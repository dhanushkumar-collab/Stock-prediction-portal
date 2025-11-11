from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.stock_list, name='stock-list'),
    path('stocks/<int:pk>/', views.stock_detail, name='stock-detail'),
]
