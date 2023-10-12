from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from src import get_db, db_dependency
from typing import Annotated
from fastapi import APIRouter, Depends
from src.models import Todo, User
from src.schema import CreateUserRequest, ProfileUpdateRequest
from .auth import get_current_user
from sqlalchemy.orm import Session
from src.routers.auth import bycrpt_context


router = APIRouter(tags=["Profile"],
                   prefix="/user")


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]


@router.get('/get_profile', status_code=200, response_model= CreateUserRequest)
async def GetProfile(user: user_dependency, db: db_dependency):
    user = db.query(User).filter(User.id == user['id']).first()
    if user:
        result =  jsonable_encoder(user)
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



@router.post('/updateprofile', status_code=201, response_model= ProfileUpdateRequest)
async def UpdateProfile(profileupdate: ProfileUpdateRequest, user: user_dependency, db: db_dependency):
    profile = db.query(User).filter(User.id == user['id']).first()
    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 
    
    profile = jsonable_encoder(profile)
    update = ProfileUpdateRequest(**profile)
    profileupdate = profileupdate.dict(exclude_unset=True, exclude_defaults=True)
    result = update.copy(update=profileupdate)
    result = jsonable_encoder(result)
   
    db.query(User).filter(Todo.id == user['id']).update(result, synchronize_session=False)
    db.commit()
    return result

@router.post('/passwordupdate', status_code= 200)
async def PasswordUpdate(user: user_dependency, db: db_dependency, old_password:str, new_password:str):
    user = db.query(User).filter(User.id == user['id']).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if  bycrpt_context.verify(old_password, user.hashed_password):
        if old_password == new_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="old password and new pasword cannot be the same")
        db.query(User).filter(User.id == user.id).update({"hashed_password":bycrpt_context.hash(new_password)}, synchronize_session=False)
        db.commit()
    return "password successfully updated"