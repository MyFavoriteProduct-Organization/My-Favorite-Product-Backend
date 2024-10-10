from fastapi import FastAPI
from routes.product_controller import product_controller
from routes.purchase_controller import purchase_controller
from routes.product_purchases_controller import product_purchase_controller

app = FastAPI()
app.include_router(product_controller)
app.include_router(purchase_controller)
app.include_router(product_purchase_controller)
