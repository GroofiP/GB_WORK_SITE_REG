
from django.contrib import admin
from django.urls import path, include, re_path
from authapp import views as authapp
from django.conf import settings
from django.conf.urls.static import static

app_name = "authapp"

urlpatterns = [
    path('login/', authapp.login, name="login"),
    path('logout/', authapp.logout, name="logout"),
    path('register/', authapp.register, name="register"),
    path('edit/', authapp.edit, name="edit"),
    path("verify/<email>/<activation_key>/", authapp.verify, name = "verify")
]
