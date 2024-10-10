from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.migration import get_db
from models.product import Product
from fastapi.exceptions import HTTPException as HttpException

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
    if product is None:
        return HttpException(status_code=404, detail="Product not found")
    return product

@product_controller.post("/", response_model=None)
def create_product(name: str, price: float, brand:str, imgUrl:str,db: Session = Depends(get_db)):
    new_product = Product(name=name,  price=price, brand=brand, imgUrl=imgUrl)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@product_controller.put("/{id}", response_model=None)
def update_product(id: int, name: str, price: float, brand:str, imgUrl:str, db: Session = Depends(get_db)):
    product_to_update = db.query(Product).filter(Product.id == id).first()
    if product_to_update is None:
        return HttpException(status_code=404, detail="Product not found")
    product_to_update.name = name
    product_to_update.price = price
    product_to_update.brand = brand
    product_to_update.imgUrl = imgUrl
    db.commit()
    db.refresh(product_to_update)
    return product_to_update


@product_controller.delete("/{id}", response_model=None)
def delete_product(id: int, db: Session = Depends(get_db)):
    product_to_delete = db.query(Product).filter(Product.id == id).first()
    if product_to_delete is None:
        return HttpException(status_code=404, detail="Product not found")
    db.delete(product_to_delete)
    db.commit()
    return "Product deleted successfully!"

