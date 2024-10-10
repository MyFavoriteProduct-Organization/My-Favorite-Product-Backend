from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from config.base import Base
from models.product import Product
from models.purchase import Purchase
from models.product_purchases import ProductPurchase
engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/my-favorite-product", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
conection = engine.connect()
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base.metadata.create_all(bind=engine)