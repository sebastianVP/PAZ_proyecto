from django.urls import path
from .views import ver_imagenes

urlpatterns = [
    path('', ver_imagenes, name='ver_imagenes'),
]