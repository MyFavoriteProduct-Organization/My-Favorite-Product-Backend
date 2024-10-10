from sqlalchemy import  Column, Integer, String, Float
from config.base import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255))
    brand = Column(String(255))
    price = Column(Float)
    imgUrl = Column(String(255))
    
    

    


