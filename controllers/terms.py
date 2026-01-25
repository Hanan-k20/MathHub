from fastapi import APIRouter, Depends, HTTPException

# SQL Alchemy
from sqlalchemy.orm import Session
from models.term import TermModel
from models.user import UserModel
# Serializers
from serializers.term import TermSchema,CreateTermSchema,UpdateTermSchema
from typing import List
# Database Connection
from database import get_db
# Middleware
from dependencies.get_current_user import get_current_user

router = APIRouter()


@router.get("/terms", response_model=List[TermSchema])
def get_terms(db: Session = Depends(get_db)):
    terms = db.query(TermModel).all()
    return terms

@router.get("/terms/{term_id}", response_model=TermSchema)
def get_single_term(term_id: int, db: Session = Depends(get_db)):
    term = db.query(TermModel).filter(TermModel.id == term_id).first()

    if not term:
        raise HTTPException(status_code=404, detail="term not found")

    return term

@router.post('/terms', response_model=TermSchema)
def create_term(term: CreateTermSchema,  db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_term = TermModel(**term.dict(), user_id=current_user.id)
   
 
    db.add(new_term)
    db.commit()
    db.refresh(new_term)

    return new_term

@router.put('/terms/{term_id}', response_model=TermSchema)
def update_term(term_id: int, term: UpdateTermSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_term = db.query(TermSchema).filter(TermSchema.id == term_id).first()

    if not db_term:
        raise HTTPException(status_code=404, detail="term not found")

    if db_term.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission Denied")

    term_form_data = term.dict(exclude_unset=True)

    for key, value in term_form_data.items():
        setattr(db_term, key, value)

    db.commit()
    db.refresh(db_term)

    return db_term

@router.delete('/terms/{term_id}')
def delete_term(term_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_term  = db.query(TermModel).filter(TermModel.id == term_id).first()

    if not db_term:
        raise HTTPException(status_code=404, detail="term not found")

    if db_term.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission Denied")

    db.delete(db_term)
    db.commit()

    return { "message": f"term with id {term_id} was deleted!" }