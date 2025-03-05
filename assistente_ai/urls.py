from django.contrib import admin
from django.urls import path, include
from .api import api


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # Rota principal da API
    path("open", include("artigos.urls")),  # Inclui as rotas do app artigos
]
