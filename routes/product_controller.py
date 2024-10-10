from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.migration import get_db
from models.product import Product

product_controller = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)

@product_controller.get("/",response_model=None)
def get_products(db: Session = Depends(get_db)):
    products =  db.query(Product).all()
    return products

@product_controller.get("/{id}", response_model=None)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    return product

@product_controller.post("/", response_model=None)
def create_product(name: str, price: float, brand:str, imgUrl:str,db: Session = Depends(get_db)):
    new_product = Product(name=name,  price=price, brand=brand, imgUrl=imgUrl)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

