from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Item (models.Model):
    class Meta(object):
        db_table = 'item'

    name = models.CharField(
        'item', blank=False, max_length=30, db_index=True
    )

    price = models.IntegerField(
        'price', blank=False, null=False, default=0 
        )

    image = CloudinaryField(
        'image', blank=True, null=True #for now
    )

    likes = models.IntegerField(
        'likes', blank=False, null=False, default=0
    )
    
    created_at = models.DateTimeField(
        'created at', blank=True, null=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'updated at', blank=True, null=True, auto_now_add=True
    )

    

    def __str__(self):
        return self.name