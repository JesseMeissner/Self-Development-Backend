from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.views import APIView
from .serializers import CartSerializer
from .models import Carts

# Create your views here.
class CartsView(mixins.ListModelMixin , mixins.CreateModelMixin, mixins.UpdateModelMixin , generics.GenericAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class CartsCreate(generics.CreateAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)