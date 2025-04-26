from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import database
from ..models import order_details as model, orders as orders_model, payments as payments_model

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



@router.post("/update_order_statuses", summary="Update all order statuses based on payments")
def update_order_statuses(db: Session = Depends(database.get_db)):
    try:
        orders = db.query(orders_model.Order).all()

        updated = 0

        for order in orders:
            if order.payments:
                if order.status != "complete":
                    order.status = "complete"
                    updated += 1
            else:
                if order.status != "pending":
                    order.status = "pending"
                    updated += 1

        db.commit()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {"updated_orders": updated}