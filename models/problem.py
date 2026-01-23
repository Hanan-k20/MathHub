# models/tea.py

from sqlalchemy import Column, Integer, String, func, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel
from .solution import SolutionModel
from .user import UserModel


class ProblemModel(BaseModel):


    __tablename__ = "problem"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    equation_LaTeX = Column(String)
    ai_Solution = Column(String)
    created_At= Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    solutions = relationship('SolutionModel', back_populates='problem', cascade="all, delete-orphan")

    user_id = Column(Integer, ForeignKey('users.id',  ondelete="CASCADE"), nullable=False)
    user = relationship('UserModel', back_populates='problems')