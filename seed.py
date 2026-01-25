# seed.py
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base # import base model
from sqlalchemy import create_engine

from models.user import UserModel
from models.problem import ProblemModel
from models.solution import SolutionModel
from models.vote import VoteModel
from models.term import TermModel

from data.problem_data import problems_list, solutions_list
from data.user_data import user_list
from config.environment import db_URI

from sqlalchemy import text


engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # Drop and recreate tables to ensure a clean slate
    db = SessionLocal()
    db.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
    db.commit()
    
    # 2. إنشاء الجداول من جديد بناءً على الموديلات المعرفة
    Base.metadata.create_all(bind=engine)
    print("Seeding the database...")
    db = SessionLocal()

    db.add_all(user_list)
    db.commit()

    # Seed teas first, as comments depend on them
    db.add_all(problems_list)
    db.commit()

    # Seed comments after teas
    db.add_all(solutions_list)
    db.commit()
    db.close()

    print("Database seeding complete! ")
except Exception as e:
    print("An error occurred:", e)
