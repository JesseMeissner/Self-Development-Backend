from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ItemsList.as_view(), name='items_list'),
    path('<int:id>', views.Item.as_view(), name='item'),
]