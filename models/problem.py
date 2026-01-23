# models/tea.py

from sqlalchemy import Column, Integer, String, func, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel
from .solution import SolutionModel
from .user import UserModel


#  TeaModel extends SQLAlchemy's Base class.
#  Extending Base lets SQLAlchemy 'know' about our model, so it can use it.

class ProblemModel(BaseModel):

    # This will be used directly to make a
    # TABLE in Postgresql
    __tablename__ = "problem"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, unique=True)
    Equation_LaTeX = Column(String)
    AI_Solution = Column(String)
    Created_At= Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    solutions = relationship('SolutionModel', back_populates='problem', cascade="all, delete-orphan")

    user_id = Column(Integer, ForeignKey('users.id',  ondelete="CASCADE"), nullable=False)
    user = relationship('UserModel', back_populates='problems')