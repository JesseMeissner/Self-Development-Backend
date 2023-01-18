from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.items.models import Item

# Create your models here.
class Carts(models.Model):
    class Meta(object):
        db_table = 'carts'

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, db_index=True , related_name='item_name_carts', blank=True, null=True
    )

    quantity = models.IntegerField(
        'quantity', blank=False, null=False, default=0, db_index=True
    )

    created_at = models.DateTimeField(
        'created at', blank=True, null=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'updated at', blank=True, null=True, auto_now=True
    )