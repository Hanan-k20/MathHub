from pydantic import BaseModel
from .user import UserSchema


class SolutionSchema(BaseModel):
  id: int
  content: str
  is_AI: bool
  user:UserSchema
  
  votes_count: int = 0  
  is_voted: bool = False 

  class Config:
    orm_mode = True


class SolutionCreateSchema(BaseModel):
  content: str
  
  

  class Config:
    orm_mode = True

class SolutionUpdateSchema(BaseModel):
  content: str
  

  class Config:
    orm_mode = True