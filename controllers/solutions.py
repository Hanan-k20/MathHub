from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.solution import SolutionModel
from models.problem import ProblemModel
from serializers.solution import SolutionCreateSchema,SolutionSchema,SolutionUpdateSchema
from typing import List
from database import get_db

router = APIRouter()

@router.get("/problems/{problem_id}/solutions", response_model=List[SolutionSchema])
def get_solutions_for_problem(problem_id: int, db: Session = Depends(get_db)):
    problem = db.query(ProblemModel).filter(ProblemModel.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem.solutions

@router.get("/solutions/{solution_id}", response_model=SolutionSchema)
def get_solutions(solution_id: int, db: Session = Depends(get_db)):
    solution = db.query(SolutionModel).filter(SolutionModel.id == solution_id).first()
    if not solution:
        raise HTTPException(status_code=404, detail="solution not found")
    return solution

@router.post("/problems/{problem_id}/solutions", response_model=SolutionSchema)
def create_solution(problem_id: int, solution: SolutionCreateSchema, db: Session = Depends(get_db)):
    problem = db.query(ProblemModel).filter(ProblemModel.id == problem_id).first()
    if not problem:
        raise HTTPException(status_code=404, detail="problem not found")

    new_solution = SolutionModel(**solution.dict(), problem_id=problem_id)
    db.add(new_solution)
    db.commit()
    db.refresh(new_solution)
    return new_solution

@router.put("/solutions/{solution_id}", response_model=SolutionSchema)
def update_solution(solution_id: int, solution: SolutionUpdateSchema, db: Session = Depends(get_db)):
    db_solution = db.query(SolutionModel).filter(SolutionModel.id == solution_id).first()
    if not db_solution:
        raise HTTPException(status_code=404, detail="solution not found")

    solution_data = solution.dict(exclude_unset=True)
    for key, value in solution_data.items():
        setattr(db_solution, key, value)

    db.commit()
    db.refresh(db_solution)
    return db_solution

@router.delete("/solutions/{solution_id}")
def delete_solution(solution_id: int, db: Session = Depends(get_db)):
    db_solution = db.query(SolutionModel).filter(SolutionModel.id == solution_id).first()
    if not db_solution:
        raise HTTPException(status_code=404, detail="solution not found")

    db.delete(db_solution)
    db.commit()
    return {"message": f"solution with ID {solution_id} has been deleted"}