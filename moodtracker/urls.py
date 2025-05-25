# moodtracker/urls.py
from django.urls import path
from . import views

app_name = 'moodtracker'

urlpatterns = [
    path('registrar/', views.registrar_humor, name='registrar_humor'),
    path('meu-historico/', views.meu_historico, name='meu_historico'),
    path('parceiro/', views.humor_parceiro, name='humor_parceiro'), # NOVA URL
]