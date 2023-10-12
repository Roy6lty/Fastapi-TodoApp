from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import and_
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from src import get_db, db_dependency
from typing import Annotated, Optional
from fastapi import APIRouter, Depends
from src.models import Todo
from src.schema import TodoSchema
from ulid import ulid
from .auth import get_current_user
from sqlalchemy.orm import Session 


router = APIRouter(tags=["Task"],
                   prefix="/todo")


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]


class LoginForm:
    def __init__(self, request: Request):
        self.request : Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None
    
    async def create_oauth_form(self):
        form =  await self.request.form() #calling itself by extention
        self.username = form.get('email')
        self.password = form.get('password')

# @router.post('/', response_class=HTMLResponse)
# async def newlogin(request: Request, db: db_dependency):
#     try: 
#         form = LoginForm(request)
#         await form.create_oauth_form()
#         response = RedirectResponse(url="/todos", status_code= 200) 



@router.post("/addtask", status_code=201, response_model=TodoSchema)
async def AddTask(task : TodoSchema, db: db_dependency, user:user_dependency):
    new_task =  Todo(id=ulid(),title=task.title, priority=task.priority, 
                     complete=task.complete, description=task.description, owner = user["id"])  
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    result = jsonable_encoder(new_task)


    return result

@router.get("/getalltask", status_code=200)
async def GetAllTasks(db: db_dependency, user: user_dependency):
    all_tasks = db.query(Todo).filter(Todo.owner == user["id"]).all()
    return all_tasks



@router.get('/gettask', status_code=200, response_model=TodoSchema)
async def gettask(task_id:str, db:db_dependency, user: user_dependency):
    
    task = db.query(Todo).filter(and_(Todo.id == task_id, Todo.owner == user["id"])).first()
    if task is None:
        raise HTTPException(status_code=400, detail="Task does not exist")
    result = jsonable_encoder(task)
    return result

@router.put('/updatetask')
async def UpdateTask(task_id:str, taskbody:TodoSchema, db:db_dependency, user: user_dependency):
    task = db.query(Todo).filter(and_(Todo.id == task_id, Todo.owner == user["id"])).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        task = jsonable_encoder(task)
        new_task = TodoSchema(**task) #coverting dictionary to data model
        
    task_update = taskbody.dict(exclude_unset=True, exclude_defaults=True) #creating data model from input fields
    task_update = new_task.copy(update=task_update)
    task_update = jsonable_encoder(task_update)

    db.query(Todo).filter(Todo.id == task_id).update(task_update, synchronize_session=False)
    db.commit()
    
    return task_update  

@router.delete('/deletetask')
async def DeleteTask(task_id:str, db:db_dependency, user: user_dependency):
    task = db.query(Todo).filter(Todo.owner == user["id"]).first()
    
    db.delete(task)
    db.commit()

    return f"task {task_id} has been deleted"
   
                            