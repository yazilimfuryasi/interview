from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('admin/', admin.site.urls),
]
