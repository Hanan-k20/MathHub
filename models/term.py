
from sqlalchemy import Column, Integer, String, func, ForeignKey,DateTime ,Enum
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel


class TermModel(BaseModel):
    CATEGORIES = [
    'Algebra',
    'Geometry',
    'Calculus',
    'Statistics',
    'Probability',
    'Trigonometry',
    'Linear Algebra',
    'Number Theory' ,
    'Discrete Math'
    ]

    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    definition = Column(String, nullable=False)
    example = Column(String, nullable=False)
    category = Column(Enum(*CATEGORIES, name="category_enum"), nullable=False)
    created_At= Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user_id = Column(Integer, ForeignKey('users.id',  ondelete="CASCADE"), nullable=False)
    user = relationship('UserModel', back_populates='terms')