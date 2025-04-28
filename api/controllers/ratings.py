from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import ratings as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_rating = model.Rating(**request.dict())
    try:
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)
        return new_rating
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    return db.query(model.Rating).all()


def read_one(db: Session, rating_id):
    rating = db.query(model.Rating).filter(model.Rating.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
    return rating


def update(db: Session, rating_id, request):
    rating = db.query(model.Rating).filter(model.Rating.id == rating_id)
    if not rating.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
    rating.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return rating.first()


def delete(db: Session, rating_id):
    rating = db.query(model.Rating).filter(model.Rating.id == rating_id)
    if not rating.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
    rating.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

