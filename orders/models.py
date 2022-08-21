from django.db import models
from accounts.models import Account
from store.models import Product, Variation

# Create your models here.
class Payment(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  payment_id = models.CharField('ID de pago', max_length=100)
  payment_method = models.CharField('Forma de pago', max_length=100)
  amount_id = models.CharField('ID de monto', max_length=100)
  status = models.CharField('Estado del pago', max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'pago'
    verbose_name_plural = 'pagos'

  def __str__(self):
    return self.payment_id

class Order(models.Model):
  STATUS = (
    ('New', 'Nuevo'),
    ('Accepted', 'Aceptado'),
    ('Completed', 'Completado'),
    ('Cancelled', 'Cancelado'),
  )

  user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
  payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
  order_number = models.CharField('Número de pedido', max_length=20)
  first_name = models.CharField('Nombres', max_length=50)
  last_name = models.CharField('Apellidos', max_length=50)
  phone = models.CharField('Teléfono', max_length=50)
  email = models.CharField('Correo electrónico', max_length=50)
  address_line_1 = models.CharField('Dirección 1', max_length=100)
  address_line_2 = models.CharField('Dirección 2', max_length=100)
  state = models.CharField('Departamento', max_length=50)
  city = models.CharField('Ciudad', max_length=50)
  country = models.CharField('País', max_length=50)
  order_note = models.TextField('Nota del pedido', max_length=200, blank=True)
  order_total = models.FloatField('Pedido total')
  tax = models.FloatField('Impuesto')
  status = models.CharField('Estado del pedido', max_length=50, choices=STATUS, default='New')
  ip = models.CharField('IP', max_length=20, blank=True)
  is_ordered = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'pedido'
    verbose_name_plural = 'pedidos'

  def __str__(self):
    return self.user.first_name

class OrderProduct(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
  user = models.ForeignKey(Account, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
  color = models.CharField('Color', max_length=50)
  size = models.CharField('Tamaño', max_length=50)
  quantity = models.IntegerField('Cantidad')
  product_price = models.FloatField('Precio')
  ordered = models.BooleanField('Ordenado', default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.product.product_name