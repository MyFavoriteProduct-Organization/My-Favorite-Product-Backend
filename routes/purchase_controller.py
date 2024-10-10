from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.migration import get_db
from models.purchase import Purchase

purchase_controller = APIRouter(
    prefix="/api/v1/purchases",
    tags=["Purchases"]
)

@purchase_controller.get("/", response_model=None)
def get_purchases(db: Session = Depends(get_db)):
    purchases = db.query(Purchase).all()
    return purchases

@purchase_controller.get("/{id}", response_model=None)
def get_purchase(id: int, db: Session = Depends(get_db)):
    purchase = db.query(Purchase).filter(Purchase.id == id).first()
    return purchase

@purchase_controller.post("/", response_model=None)
def create_purchase( amount: float, db: Session = Depends(get_db)):
    new_purchase = Purchase(amount=amount)
    db.add(new_purchase)
    db.commit()
    db.refresh(new_purchase)  
    return new_purchase

