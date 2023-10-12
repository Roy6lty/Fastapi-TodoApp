from fastapi import APIRouter, Depends, status
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.schema import CreateUserPassword, CreateUserRequest
from src import get_db
from src.models import User
from ulid import ulid
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from fastapi.security import  OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from src.models import User
from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from typing import Optional
import sys
sys.path.append("..")



templates = Jinja2Templates(directory="templates")



router = APIRouter(tags =["web"])

SECRET_KEY = "hhiffs3ad74a2d46s7v897c55g43j2jfg"
ALGORITHIM = 'HS256'

class Token(BaseModel):
    access_token: str
    token_type: str








bycrpt_context= CryptContext(schemes=['bcrypt'], deprecated= 'auto')
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
db_dependency = Annotated[Session, Depends(get_db)]

templates = Jinja2Templates(directory="templates")


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get('email')
        self.password = form.get('password')

   

def AuthenticateUser(username:str, password:str, db:db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bycrpt_context.verify(password, user.hashed_password):
        return False
    return user

def CreateAccessToken(username: str, user_id: str, user_role:str, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id, "role":user_role}
    expires = datetime.utcnow() +  expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHIM)

async def get_current_user(request: Request):
    try:
        token = request.cookies.get('access_token')
        if token is None:
            return None
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHIM])
        username: str = payload.get("sub")
        id: str = payload.get("id")
        role: str = payload.get("role")
        if username is None or id is None:
            return None
        return {"username": username, "id": id, "role": role}
    except JWTError:
         return None
        
    

@router.post("/token")
async def AccessToken(response: Response, form_data: Annotated[OAuth2PasswordRequestForm,  Depends()], db :db_dependency):

    user = AuthenticateUser(form_data.username, form_data.password, db)
    if not user:
        return False

    token = CreateAccessToken(user.username, user.id, user.role, timedelta(minutes=5))
    response.set_cookie(key='access_token', value=token, httponly=True)

    return True
    

@router.get('/login', response_class=HTMLResponse)
async def authentication_page(request: Request):
    return templates.TemplateResponse('login.html',{"request":request})

@router.post('/login', response_class=HTMLResponse)
async def Login(request: Request, db:db_dependency):
    try:
        form = LoginForm(request)
        await form.create_oauth_form()
        response = RedirectResponse(url='/home', status_code=status.HTTP_302_FOUND)
        validate_user_cookie = await AccessToken(response=response, form_data=form, db=db)
        
        
        if not validate_user_cookie:
            msg= "incorrect Username or Password"
            return templates.TemplateResponse('login.html',{"request":request, "msg":msg})
        return response
        
    except HTTPException:
        msg ="unknown error"
        return templates.TemplateResponse('login.html',{"request":request, "msg":msg})
    