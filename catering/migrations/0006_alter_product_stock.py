# Generated by Django 5.1.3 on 2024-11-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0005_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
