# Generated by Django 4.1.3 on 2023-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_item_clicked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated at'),
        ),
    ]
