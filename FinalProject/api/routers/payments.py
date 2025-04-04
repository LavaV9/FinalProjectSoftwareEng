from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import payments as controller
from ..schemas import payments as schema

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/", response_model=schema.Payment)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Payment])
def get_all_payments(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{item_id}", response_model=schema.Payment)
def get_payment(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Payment)
def update_payment(item_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
