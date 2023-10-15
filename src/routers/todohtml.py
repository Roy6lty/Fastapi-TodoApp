import sys
sys.path.append("..")
from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from src import get_db
from typing import Annotated
from fastapi import APIRouter, Depends
from .authhtml import get_current_user
from sqlalchemy.orm import Session 
from fastapi.templating import Jinja2Templates
from src import models
from ulid import ulid
from typing import Optional
from . import authhtml
from src.celery import countdown 


router = APIRouter(tags=["web"])

db_dependency = Annotated[Session, Depends(get_db)]
templates = Jinja2Templates(directory="templates")


@router.get('/home', response_class=HTMLResponse)
async def HomePage(request: Request, db: db_dependency):
    user_dict = await get_current_user(request=request)
    if user_dict is None:
         return RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    todo = db.query(models.Todo).filter(models.Todo.owner == user_dict.get('id')).all()
    countdown.delay(10)

    return templates.TemplateResponse("home.html", {"request": request, "todo":todo, 'user':user_dict})


@router.get('/add_todo', response_class=HTMLResponse)
async def AddTodo(request: Request):
    user_dict = await get_current_user(request=request)
    return templates.TemplateResponse("add_todo.html", {"request": request, 'user':user_dict})

@router.post('/add_todo', response_class=HTMLResponse)
async def CreateTodo(request: Request, db:db_dependency, title: str= Form(...), description: str= Form(...), 
                                priority: int = Form(...)):
    user_dict = await get_current_user(request=request)
    if user_dict is None:
         return RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    
    
    todo_model = models.Todo()
    todo_model.id = ulid()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority
    todo_model.owner = user_dict.get('id')

    db.add(todo_model)
    db.commit()
    return RedirectResponse(url='/home', status_code=status.HTTP_302_FOUND)


@router.get('/edit_todo/{todo_id}', response_class=HTMLResponse)
async def EditTodo(request: Request, todo_id : str, db:db_dependency):
    user_dict = await get_current_user(request=request)
    if user_dict is None:
         return RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return templates.TemplateResponse("edit_todo.html", {"request": request, 'todo':todo, 'user':user_dict})



@router.post('/edit_todo/{todo_id}' , response_class=HTMLResponse)
async def EditTodo(request: Request, todo_id : str, db:db_dependency,
                   description:str = Form(...), title:str =Form(...), priority:int = Form(...)):
    db.query(models.Todo).filter(models.Todo.id == todo_id).update({"description":description, "title":title, "priority":priority})
    db.commit()

   
    return RedirectResponse(url='/home',  status_code=status.HTTP_302_FOUND )



@router.get('/delete_todo/{todo_id}', response_class=HTMLResponse)
async def DeleteTodo(request: Request, todo_id : str, db:db_dependency):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        
    return RedirectResponse(url='/home',  status_code=status.HTTP_302_FOUND )

@router.get('/complete/{todo_id}')
async def CompleteTask(request: Request, todo_id : str, db:db_dependency):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.add(todo)
    db.commit()

    return RedirectResponse(url='/home',  status_code=status.HTTP_302_FOUND )



    