"""
Usamos las vistas de autenticación que trae Django (no reinventamos el login).
Referencia: https://docs.djangoproject.com/en/5.2/topics/auth/default/#module-django.contrib.auth.views
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LibretaLoginForm

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=LibretaLoginForm,
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
]
