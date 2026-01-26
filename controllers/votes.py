from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.vote import VoteModel
from models.solution import SolutionModel
from models.problem import ProblemModel
from serializers.vote import VoteCreateSchema,VoteSchema
from typing import List
from database import get_db
from models.user import UserModel
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/problems/{problem_id}/solutions/{solution_id}/votes", response_model=List[VoteSchema])
def get_votes(problem_id: int,solution_id:int, db: Session = Depends(get_db)):
    solution = db.query(SolutionModel).filter(SolutionModel.id == solution_id).first()
    if not solution:
        raise HTTPException(status_code=404, detail="vote not found")
    return solution.votes



@router.get("/votes/{vote_id}", response_model=VoteSchema)
def get_vote_by_id(vote_id: int, db: Session = Depends(get_db)):
    vote = db.query(VoteModel).filter(VoteModel.id == vote_id).first()
    if not vote:
        raise HTTPException(status_code=404, detail="vote not found")
    return vote


@router.post("/problems/{problem_id}/solutions/{solution_id}/votes")
def toggle_vote(problem_id: int, solution_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    solution = db.query(SolutionModel).filter(SolutionModel.id == solution_id).first()
    if not solution:
        raise HTTPException(status_code=404, detail="Solution not found")

    existing_vote = db.query(VoteModel).filter(
        VoteModel.solution_id == solution_id,
        VoteModel.user_id == current_user.id
    ).first()

    if existing_vote:
        db.delete(existing_vote)
        db.commit()
        return {"voted": False, "total_votes": len(solution.votes)}

    new_vote = VoteModel(solution_id=solution_id, user_id=current_user.id)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    
    return {"voted": True, "total_votes": len(solution.votes)}