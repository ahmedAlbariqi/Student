from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← هذا هو المطلوب
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
