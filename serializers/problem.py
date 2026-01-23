# serializers/tea.py

from pydantic import BaseModel
from typing import Optional, List
from .solution import SolutionSchema
from .user import UserSchema

# Whenever we send out json this will be our response
class ProblemSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  title: str
  equation_LaTeX: str
  ai_Solution: str
  created_At: datatime
  user: UserSchema
  Solutions: List[SolutionSchema] = []

  class Config:
    orm_mode = True

# These two below are specifically for req.body
class CreateProblemSchema(BaseModel):
  name: str
  in_stock: bool
  rating: int

  class Config:
    orm_mode = True

class UpdateProblemSchema(BaseModel):
  name: str
  in_stock: bool
  rating: int

  class Config:
    orm_mode = True