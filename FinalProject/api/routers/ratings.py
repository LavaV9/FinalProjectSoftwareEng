from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import ratings as controller
from ..schemas import ratings as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)

@router.post("/", response_model=schema.Rating)
def create_rating(request: schema.RatingCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)


@router.get("/", response_model=list[schema.Rating])
def get_all_ratings(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{rating_id}", response_model=schema.Rating)
def get_one_rating(rating_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, rating_id)


@router.put("/{rating_id}", response_model=schema.Rating)
def update_rating(rating_id: int, request: schema.RatingUpdate, db: Session = Depends(get_db)):
    return controller.update(db, rating_id, request)


@router.delete("/{rating_id}")
def delete_rating(rating_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, rating_id)

