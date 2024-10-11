from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from config.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    brand = Column(String(255), index=True)
    price = Column(Float)
    discount_price = Column(Float)
    image_url = Column(String(1024)) # aceptar cadenas de longitud alta
    quantity = Column(String(255))
    category = Column(String(255), index=True)
    subcategory = Column(String(255), index=True)
    absolute_url = Column(String(1024))
    purchases = relationship("ProductPurchase", back_populates="product", cascade="all, delete")