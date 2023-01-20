from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CartsView.as_view(), name='carts_list'),
    path('create/', views.CartsCreate.as_view(), name='carts_create'),
    path('update/<int:item_id>/', views.CartsUpdate.as_view(), name='carts_update')
]