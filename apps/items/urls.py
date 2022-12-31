from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ItemsList.as_view(), name='items_list')
]