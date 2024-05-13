from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/add/', views.add_item, name='add_item'),
    path('item/<int:pk>/update/', views.update_quantity, name='update_quantity'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
]
