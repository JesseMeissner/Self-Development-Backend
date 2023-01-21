from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Categories

# Create your models here.
class Item (models.Model):
    class Meta(object):
        db_table = 'item'

    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, db_index=True , related_name='item_category', blank=True, null=True
    )

    name = models.CharField(
        'name', blank=False, max_length=30, db_index=True, null=False, default='item'
    )

    price = models.IntegerField(
        'price', blank=False, null=False, default=0 
        )

    image = CloudinaryField(
        'image', blank=True, null=True #for now
    )

    created_at = models.DateTimeField(
        'created at', blank=True, null=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'updated at', blank=True, null=True, auto_now=True
    )

    

    def __str__(self):
        return self.name