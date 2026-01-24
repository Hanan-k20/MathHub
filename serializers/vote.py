from pydantic import BaseModel
from .user import UserSchema
from datetime import datetime


class VoteSchema(BaseModel):
  id: int
  solution_id: int
  created_at: datetime
  user:UserSchema
  
  

  class Config:
    orm_mode = True


class VoteCreateSchema(BaseModel):
  solution_id: int
  
  

  class Config:
    orm_mode = True

