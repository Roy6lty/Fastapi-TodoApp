from fastapi import APIRouter
from sqlalchemy import insert, update
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from src import get_db, db_dependency
from typing import Annotated
from fastapi import APIRouter, Depends
from .models import Todo
from .schema import TodoFull,TodoSchema
from ulid import ulid


router = APIRouter()


@router.post("/addtask", status_code=201, response_model=TodoSchema)
async def AddTask(task : TodoFull, db: db_dependency):
    new_task =  Todo(id=ulid(),title=task.title, priority=task.priority, complete=task.complete, description=task.description)  
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    result = jsonable_encoder(new_task)


    return result

@router.get("/getalltask", status_code=200)
async def GetAllTasks(db: db_dependency):
    all_tasks = db.query(Todo).all()
    # result = jsonable_encoder(all_tasks)
    return all_tasks



@router.get('/gettask', status_code=200, response_model=TodoSchema)
async def gettask(task_id:str, db:db_dependency):
    
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=400, detail="User id does not exist")
    result = jsonable_encoder(task)
    return result

@router.put('/updatetask')
async def UpdateTask(task_id:str, taskbody:TodoSchema, db:db_dependency):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        task = jsonable_encoder(task)
        new_task = TodoSchema(**task) #coverting dictionary to data model
        
    task_update = taskbody.dict(exclude_unset=True, exclude_defaults=True) #creating data model from input fields
    task_update = new_task.copy(update=task_update)
    db_task = task_update.dict()
    task_update = jsonable_encoder(task_update)

    db.query(Todo).filter(Todo.id == task_id).update(task_update, synchronize_session=False)
    db.commit()
    
    return task_update  

@router.delete('/deletetask')
async def DeleteTask(task_id:str, db:db_dependency):
    task = db.query(Todo).get(task_id)
    db.delete(task)
    db.commit()

    return f"task {task_id} has been deleted"
   
                            