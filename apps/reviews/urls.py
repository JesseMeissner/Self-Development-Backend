from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='reviews_list')
]