from fastapi import FastAPI
from app.config import get_settings
from app.routes.sales import router as router_sales
from app.routes.cities import router as router_cities
from app.routes.products import router as router_products
from app.routes.stores import router as router_stores
from app.routes.methods import router as router_methods

app = FastAPI(debug=get_settings().debug)
app.include_router(router_sales, prefix="/api", tags=["sales"])
app.include_router(router_cities, prefix="/api", tags=["cities"])
app.include_router(router_products, prefix="/api", tags=["products"])
app.include_router(router_stores, prefix="/api", tags=["stores"])
app.include_router(router_methods, prefix="/api", tags=["methods"])
