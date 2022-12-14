# Generated by Django 4.1 on 2022-08-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'variación', 'verbose_name_plural': 'variaciones'},
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='photos/products', verbose_name='Subir imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'Color'), ('talla', 'Talla')], max_length=100, verbose_name='Variaciónes'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(max_length=100, verbose_name='Valores'),
        ),
    ]
