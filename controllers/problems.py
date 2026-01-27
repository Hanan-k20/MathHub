from fastapi import APIRouter, Depends, HTTPException

# SQL Alchemy
from sqlalchemy.orm import Session
from models.problem import ProblemModel
from models.user import UserModel
from services.ai_service import solve_math
# Serializers
from serializers.problem import ProblemSchema, CreateProblemSchema, UpdateProblemSchema
from typing import List
# Database Connection
from database import get_db
# Middleware
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/problems", response_model=List[ProblemSchema])
def get_problems(db: Session = Depends(get_db)):
    # Get all
    problems = db.query(ProblemModel).all()
    return problems

@router.get("/problems/{problem_id}", response_model=ProblemSchema)
def get_single_problem(problem_id: int, db: Session = Depends(get_db)):
    problem = db.query(ProblemModel).filter(ProblemModel.id == problem_id).first()

    if not problem:
        raise HTTPException(status_code=404, detail="problem not found")

    return problem

@router.post('/problems', response_model=ProblemSchema)
def create_problem(problem: CreateProblemSchema,  db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_problem = ProblemModel(**problem.dict(), user_id=current_user.id)
    
    ai_solution = solve_math(new_problem.equation_LaTeX) 
    new_problem.ai_solution = ai_solution 
    
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)

    return new_problem

@router.put('/problems/{problem_id}', response_model=ProblemSchema)
def update_problem(problem_id: int, problem: UpdateProblemSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_problem  = db.query(ProblemModel).filter(ProblemModel.id == problem_id).first()

    if not db_problem:
        raise HTTPException(status_code=404, detail="problem not found")

    if db_problem.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission Denied")

    problem_form_data = problem.dict(exclude_unset=True)
    
    if "equation_LaTeX" in problem_form_data:
        new_equation = problem_form_data["equation_LaTeX"]
        db_problem.ai_solution = solve_math(new_equation)

    for key, value in problem_form_data.items():
        setattr(db_problem, key, value)

    db.commit()
    db.refresh(db_problem)

    return db_problem

@router.delete('/problems/{problem_id}')
def delete_problem(problem_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_problem  = db.query(ProblemModel).filter(ProblemModel.id == problem_id).first()

    if not db_problem:
        raise HTTPException(status_code=404, detail="problem not found")

    if db_problem.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Permission Denied")

    db.delete(db_problem)
    db.commit()

    return { "message": f"problem with id {problem_id} was deleted!" }

@router.get("/cards")
def get_all_cards(db: Session = Depends(get_db)):
    problems = db.query(ProblemModel).all()
    return problems 

