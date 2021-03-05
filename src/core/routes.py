from fastapi import APIRouter
from src.service import views
from src.api import views as api_views

# service route
service_routes = APIRouter()
service_routes.include_router(views.router, prefix="/service")

# api route
api_routes = APIRouter()
api_routes.include_router(api_views.router, prefix="/api")
