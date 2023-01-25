from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import action
from .serializers import CartSerializer
from .models import Carts

# Create your views here.
class CartsView(mixins.ListModelMixin , mixins.CreateModelMixin, mixins.UpdateModelMixin , generics.GenericAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'item_id'

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class CartsCreate(generics.CreateAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)
        



class CartsUpdate(UpdateAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'item_id'

    def update(self, request, *args, **kwargs):
        cart = self.get_object()
        cart.quantity += 1
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)



class CartsDecrement(UpdateAPIView):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'item_id'

    def update(self, request, *args, **kwargs):
        cart = self.get_object()
        cart.quantity -= 1
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)