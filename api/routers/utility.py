from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import database
from ..models import order_details as model

router = APIRouter(
    prefix="/utility",
    tags=["Utility"],
)

@router.get("/total_revenue", summary="Get total revenue generated")
def total_revenue(db: Session = Depends(database.get_db)):
    try:
        order_details = db.query(model.OrderDetail).all()
        revenue = sum(od.price for od in order_details)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return {"total_revenue": revenue}
