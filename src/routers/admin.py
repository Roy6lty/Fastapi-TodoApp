from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src import get_db, db_dependency
from typing import Annotated
from fastapi import APIRouter, Depends
from src.models import Todo
from .auth import get_current_user
from sqlalchemy.orm import Session


router = APIRouter(tags=["Admin"],
                   prefix="/admin")


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/todo", status_code=200)
async def GetAllTasks(user: user_dependency, db:db_dependency):
    if user['role'] != 'admin':
        raise HTTPException(status_code=401, detail="NOT Authorized to access this route")
    all_tasks = db.query(Todo).all()
    return all_tasks