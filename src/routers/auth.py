from fastapi import APIRouter, Depends
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
from fastapi.responses import HTMLResponse



templates = Jinja2Templates(directory="templates")



router = APIRouter(tags =["Auth"], prefix="/auth")

SECRET_KEY = "hhiffs3ad74a2d46s7v897c55g43j2jfg"
ALGORITHIM = 'HS256'

class Token(BaseModel):
    access_token: str
    token_type: str




db_dependency =  Annotated[Session, Depends(get_db)]

bycrpt_context= CryptContext(schemes=['bcrypt'], deprecated= 'auto')

oauth_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")



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

# async def get_current_user(token: Annotated[str, Depends(oauth_scheme)]):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHIM])
#         username: str = payload.get("sub")
#         id: str = payload.get("id")
#         role: str = payload.get("role")
#         if username is None or id is None:
#             raise HTTPException(status_code=401,
#                                 detail="could not validate user")
#         return {"username": username, "id": id, "role": role}
#     except JWTError:
#          raise HTTPException(status_code=401,
#                                 detail="could not validate user")
        
def get_current_user():
    pass

@router.post("/token", response_model=Token)
async def AccessToken(form_data: Annotated[OAuth2PasswordRequestForm,  Depends()], db :db_dependency):
    user = AuthenticateUser(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401,
                                detail="could not validate user")

    token = CreateAccessToken(user.username, user.id, user.role, timedelta(minutes=5))
    return {"access_token": token, "token_type": "bearer"}
    


@router.post("/create_user", response_model=CreateUserRequest, status_code=201)
async def CreateUser(user: CreateUserPassword, db:db_dependency):
    usercreate = user.copy(exclude={"password"})
    createuser = User(id=ulid(), **usercreate.dict(), hashed_password=bycrpt_context.hash(user.password))
    db.add(createuser)
    db.commit()
    db.refresh(createuser)

    result= jsonable_encoder(createuser)


    return result










