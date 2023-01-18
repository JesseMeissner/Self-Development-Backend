from django.db import models
from django.core.validators import MaxValueValidator
from apps.items.models import Item 

# Create your models here.
class Reviews(models.Model):
    class Meta(object):
        db_table = 'review'

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, db_index=True , related_name='item_name_reviews', blank=True, null=True
    )

    name = models.CharField(
        blank=False, null=False, max_length=30
    )

    likes = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(4)]
    )

    review = models.CharField(
        blank=False, null=False, max_length=250
    )

    def __str__(self):
        return self.name