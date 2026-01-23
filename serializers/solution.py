from pydantic import BaseModel

class SolutionSchema(BaseModel):
  id: int
  content: str

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