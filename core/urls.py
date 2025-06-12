from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre_mim, name='sobre_mim'),
    path('projetos/', views.projetos, name='projetos'),
    path('certificados/', views.certificados, name='certificados'),
    path('fale-comigo/', views.fale_comigo, name='fale_comigo'),
]
