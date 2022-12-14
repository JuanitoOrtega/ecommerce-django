# Generated by Django 4.1 on 2022-08-21 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_alter_product_options_alter_variation_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, verbose_name='Número de pedido')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('phone', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('email', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('address_line_1', models.CharField(max_length=100, verbose_name='Dirección 1')),
                ('address_line_2', models.CharField(max_length=100, verbose_name='Dirección 2')),
                ('state', models.CharField(max_length=50, verbose_name='Departamento')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('country', models.CharField(max_length=50, verbose_name='País')),
                ('order_note', models.TextField(blank=True, max_length=200, verbose_name='Nota del pedido')),
                ('order_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Nuevo'), ('Accepted', 'Aceptado'), ('Completed', 'Completado'), ('Cancelled', 'Cancelado')], default='New', max_length=50, verbose_name='Estado del pedido')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='IP')),
                ('is_ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, verbose_name='ID de pago')),
                ('payment_method', models.CharField(max_length=100, verbose_name='Forma de pago')),
                ('amount_id', models.CharField(max_length=100, verbose_name='ID de monto')),
                ('status', models.CharField(max_length=100, verbose_name='Status del pago')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pago',
                'verbose_name_plural': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('size', models.CharField(max_length=50, verbose_name='Tamaño')),
                ('quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.variation')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
