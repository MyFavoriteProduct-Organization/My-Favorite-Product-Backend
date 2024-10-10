from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base
class ProductPurchase(Base):
    __tablename__ = "product_purchases"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"), primary_key=True)
    product = relationship("Product", back_populates="purchases", cascade="all, delete")
    purchase = relationship("Purchase", back_populates="products", cascade="all, delete")