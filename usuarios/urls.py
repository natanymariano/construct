from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name="cadastrar_vendedor"),
    path('liberar_descontos/', views.liberar_descontos, name="liberar_descontos")
]