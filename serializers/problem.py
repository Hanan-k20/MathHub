
from pydantic import BaseModel
from typing import Optional, List
from .solution import SolutionSchema
from datetime import datetime 
from .user import UserSchema

# Whenever we send out json this will be our response
class ProblemSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  title: str
  equation_LaTeX: str
  ai_solution: str
  created_At: datetime
  user: UserSchema
  Solutions: List[SolutionSchema] = []

  class Config:
    orm_mode = True

# These two below are specifically for req.body
class CreateProblemSchema(BaseModel):
  title: str
  equation_LaTeX: str


  class Config:
    orm_mode = True

class UpdateProblemSchema(BaseModel):
  title: str
  equation_LaTeX: str


  class Config:
    orm_mode = True