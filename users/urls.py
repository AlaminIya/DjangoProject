from django.urls import path, include
from users.views import dashboard 
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", views.register_request, name="register"),
]