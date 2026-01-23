# seed.py
from sqlalchemy.orm import Session, sessionmaker
from data.problem_data import problems_list, solutions_list
from data.user_data import user_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base # import base model

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # Drop and recreate tables to ensure a clean slate
    Base.metadata.drop_all(bind=engine)
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
