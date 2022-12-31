from django.db import models

# Create your models here.
class Carts(models.Model):
    class Meta(object):
        db_table = 'carts'

    items = models.CharField(
        'items', blank=False, null=False, max_length=40,
    )