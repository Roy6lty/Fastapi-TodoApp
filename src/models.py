from .database import Base
from sqlalchemy import Column,String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ ="todos"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner = Column(String, ForeignKey("users.id"))
    #ower_id = relationship(backpoplates="users.owner")

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, index=True)
    email = Column(String)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String)
    role = Column(String)
    #todo = relationship(backpoplates="todos.ower_id")




