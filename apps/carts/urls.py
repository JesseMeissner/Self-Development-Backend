from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CartsView.as_view(), name='carts_list'),
    path('create/', views.CartsCreate.as_view(), name='carts_create'),
    path('<int:item_id>/update', views.CartsUpdate.as_view(), name='carts_update'),
    path('<int:item_id>/decrement', views.CartsDecrement.as_view(), name='carts_decrement')

]