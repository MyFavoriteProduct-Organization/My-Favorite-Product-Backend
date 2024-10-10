from sqlalchemy import  Column, Integer, ForeignKey
from config.base import Base
class ProductPurchase(Base):
    __tablename__ = "product_purchases"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"), primary_key=True)