import csv
import os
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

def populate_products_from_csv(db: Session):
    # extraer de la ruta raiz del proyecto
    csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'BigBasket.csv')
    try:
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(
                    name=row['ProductName'],
                    brand=row['Brand'],
                    price=float(row['Price']),
                    discount_price=float(row['DiscountPrice']),
                    image_url=row['Image_Url'],
                    quantity=row['Quantity'],
                    category=row['Category'],
                    subcategory=row['SubCategory'],
                    absolute_url=row['Absolute_Url']
                )
                db.add(product)
            db.commit()
            print("Products populated successfully from CSV.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        raise e