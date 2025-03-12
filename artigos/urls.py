from django.urls import path
from . import views


urlpatterns = [
    path("/dashboard/", views.dashboard, name="dashboard"),
    path("/criar_artigo/", views.criar_artigo, name="criar_artigo"),
    path("/settings/", views.settings, name="settings"),
]
