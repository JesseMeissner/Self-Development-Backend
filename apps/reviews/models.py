from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Reviews(models.Model):
    class Meta(object):
        db_table = 'review'

    name = models.CharField(
        blank=False, null=False, max_length=30
    )

    likes = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(4)]
    )

    review = models.CharField(
        blank=False, null=False, max_length=250
    )