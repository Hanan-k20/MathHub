from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class VoteModel(BaseModel):

  __tablename__ = "votes"

  id = Column(Integer, primary_key=True, index=True)
  
  # relationships
  solution_id = Column(Integer, ForeignKey('solutions.id', ondelete="CASCADE"), nullable=False)
  solution = relationship("SolutionModel", back_populates="votes")

  user_id = Column(Integer, ForeignKey('users.id',  ondelete="CASCADE"), nullable=False)
  user = relationship('UserModel', back_populates='votes')