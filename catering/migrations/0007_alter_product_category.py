# Generated by Django 5.1.3 on 2024-11-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering', '0006_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='Snacks', max_length=100),
        ),
    ]
