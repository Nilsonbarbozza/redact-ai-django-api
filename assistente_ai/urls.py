from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from artigos.api import router as artigos_router

api = NinjaAPI(title="Assistente de Escrita AI")

api.add_router("/artigos", artigos_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # Rota principal da API
]
