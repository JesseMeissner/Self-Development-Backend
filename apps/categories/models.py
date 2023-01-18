from django.db import models

# Create your models here.
class Categories(models.Model):
    class Meta(object):
        db_table = 'categories'

    category = models.CharField(
        'category', blank=False, null=False,max_length=20, db_index=True, default='category'
    )

    def __str__(self):
        return self.category