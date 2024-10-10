from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.migration import get_db
from models.product_purchases import ProductPurchase

product_purchase_controller = APIRouter(
    prefix="/api/v1/product_purchases",
    tags=["Product Purchases"]
)

@product_purchase_controller.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(ProductPurchase).all()

@product_purchase_controller.get("/get-by-product-id/{product_id}", response_model=None)
def get_by_product_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductPurchase).filter(ProductPurchase.product_id == product_id).all()
    return product


@product_purchase_controller.get("/get-by-purchase-id/{purchase_id}", response_model=None)
def get_by_purchase_id(purchase_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductPurchase).filter(ProductPurchase.purchase_id == purchase_id).all()
    return product

@product_purchase_controller.post("/")
def create_product_purchase(product_id: int, purchase_id: int, db: Session = Depends(get_db)):
    product_purchase = ProductPurchase(product_id=product_id, purchase_id=purchase_id)
    db.add(product_purchase)
    db.commit()
    return {"message": "Product Purchase created successfully!"}