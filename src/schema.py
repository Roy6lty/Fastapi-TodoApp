from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class TodoSchema(BaseModel):
    title:Optional[str] | None ="string"
    description:Optional[str]  | None = "string"
    priority:Optional[int] | None = 0
    complete:Optional[bool] | None  = False
    class config:
         orm_mode = True

class TodoFull(TodoSchema):
     id:str

class CreateUserRequest(BaseModel):
    username:str 
    email: EmailStr
    firstname:str
    lastname:str
    role:str

class CreateUserPassword(CreateUserRequest):
    password: str
    
class CreateUserFull(CreateUserRequest):
     id: str



class ProfileUpdateRequest(BaseModel):
    username:Optional[str] = "string" 
    email: Optional[EmailStr] = "user@example.com"
    firstname:Optional[str] = 'string'
    lastname:Optional[str] = "string"
    role:Optional[str] = 'string'
   