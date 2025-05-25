# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe as views de autenticação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('humor/', include('moodtracker.urls')),

    # URLs de Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='moodtracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Redireciona para login após logout
    # Você também pode adicionar URLs para mudança de senha, etc., depois.
]