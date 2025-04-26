from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import database
from ..models import order_details as model, orders as orders_model, promotions as promotions_model
from datetime import datetime

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

@router.post("/apply_promo_code", summary="Apply promo code to an order")
def apply_promo_code(order_id: int, promo_code: str, db: Session = Depends(database.get_db)):
    try:
        order = db.query(orders_model.Order).filter(orders_model.Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        order_details = db.query(model.OrderDetail).filter(model.OrderDetail.order_id == order_id).all()
        if not order_details:
            raise HTTPException(status_code=404, detail="No order details found for this order")

        original_price = sum(od.price for od in order_details)

        promo = db.query(promotions_model.Promotion).filter(promotions_model.Promotion.code == promo_code).first()
        if not promo:
            raise HTTPException(status_code=404, detail="Promo code not found")

        # Check expiration
        if promo.expiration_date < datetime.utcnow().date():
            raise HTTPException(status_code=400, detail="Promo code has expired")

        # Apply discount
        discount_amount = (promo.discount_percentage / 100) * original_price
        new_price = original_price - discount_amount

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {
        "order_id": order_id,
        "original_price": round(original_price, 2),
        "discount_percentage": promo.discount_percentage,
        "discount_amount": round(discount_amount, 2),
        "new_price_after_discount": round(new_price, 2),
    }

