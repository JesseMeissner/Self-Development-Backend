from .models import Carts
from rest_framework import serializers
from ..items.models import Item
from ..items.serializers import ItemSerializer

class CartSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(required=True, queryset=Item.objects.all())
    item_serialized = serializers.SerializerMethodField()
    
    class Meta:
        model = Carts
        fields = ('item', 'quantity', 'item_serialized')
        depth = 1

    def get_item_serialized(self, obj):
        item = obj.item
        serializer = ItemSerializer(item)
        return serializer.data