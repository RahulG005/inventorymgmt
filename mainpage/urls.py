from . import views
from django.urls import path, include


urlpatterns = [
    path('dashboard/',views.main_page, name ='dashboard'),
    path('', views.login_view, name='login'),  # Landing page as login
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

]