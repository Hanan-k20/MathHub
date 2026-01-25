# serializers/tea.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime 
from .user import UserSchema

# Whenever we send out json this will be our response
class TermSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  definition: str
  example: str
  category: str
  created_At: datetime
  user: UserSchema
  
  class Config:
    orm_mode = True

# These two below are specifically for req.body
class CreateTermSchema(BaseModel):
  name: str
  definition: str
  example: str
  category: str


  class Config:
    orm_mode = True

class UpdateTermSchema(BaseModel):
  name: str
  definition: str
  example: str
  category: str


  class Config:
    orm_mode = True