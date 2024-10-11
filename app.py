from config.cors import create_app
from routes.product_controller import product_controller
from routes.product_purchases_controller import product_purchase_controller
from routes.purchase_controller import purchase_controller
from config.migration import engine, Base

app = create_app(enable_cors=True)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(product_controller)
app.include_router(product_purchase_controller)
app.include_router(purchase_controller)