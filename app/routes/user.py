from ..db_connect import SessionLocal
from fastapi import APIRouter, FastAPI, Depends, Form, HTTPException, Request
from ..model import Users
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users

@router.post("/add_user")
async def add_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    user_model = Users(name=name, email=email)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)  # Refresh to get the user_model's updated state
    return {"message": "User added successfully", "user": user_model}
