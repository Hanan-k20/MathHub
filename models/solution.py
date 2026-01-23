from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SolutionModel(BaseModel):

  __tablename__ = "solutions"

  id = Column(Integer, primary_key=True, index=True)
  content = Column(String, nullable=False)
  is_AI = Column(bool, default=False)

  # relationships
  problem_id = Column(Integer, ForeignKey('problems.id', ondelete="CASCADE"), nullable=False)
  problem = relationship('ProblemModel', back_populates='solutions', passive_deletes=True)
  
  user_id = Column(Integer, ForeignKey('users.id',  ondelete="CASCADE"), nullable=False)
  user = relationship('UserModel', back_populates='comments')