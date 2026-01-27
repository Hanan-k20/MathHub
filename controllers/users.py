
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from serializers.user import UserSchema, UserRegistrationSchema, UserLoginSchema, UserTokenSchema
from database import get_db

router = APIRouter()

@router.post("/register", response_model=UserTokenSchema)
def create_user(user: UserRegistrationSchema, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(
        (UserModel.username == user.username) | (UserModel.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Username or email already exists")

    try:
        new_user = UserModel(username=user.username, email=user.email)
        new_user.set_password(user.password)
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        token = new_user.generate_token()

        return {
            "token": token,
            "message": "User created and logged in successfully",
            "username": user.username, 
            "email": user.email         
        }
        
    # return new_user

    except Exception as e:
        print(f"CRITICAL ERROR DURING REGISTER: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
    
    
@router.post("/login", response_model=UserTokenSchema)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):

    # Find the user by username
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    # Check if the user exists and if the password is correct
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    token = db_user.generate_token()

    # Return token and a success message
    return {"token": token, "message": "Login successful"}