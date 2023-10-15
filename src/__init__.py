from fastapi import FastAPI, Depends
from src import models
from .database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles


models.Base.metadata.create_all(bind=engine)

#database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency =  Annotated[Session, Depends(get_db)]        
from src.routers import todo, auth, admin, userprofile,todohtml, authhtml,mail



app = FastAPI()
app.include_router(todo.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(userprofile.router)
app.include_router(todohtml.router)
app.include_router(authhtml.router)
app.include_router(mail.router)

app.mount("/static", StaticFiles(directory="static"),name="static") 