from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
  product_name = models.CharField('Nombre del producto', max_length=200, unique=True)
  slug = models.CharField(max_length=200, unique=True)
  description = models.TextField('Descripción', max_length=500, blank=True)
  price = models.DecimalField('Precio', max_digits=6, decimal_places=2)
  images = models.ImageField('Images', upload_to='photos/products')
  stock = models.IntegerField('Cantidad disponible')
  is_available = models.BooleanField('Disponible', default=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_date = models.DateTimeField('Fecha de creación', auto_now_add=True)
  modified_date = models.DateTimeField('Última actualización', auto_now=True)

  def get_url(self):
    return reverse('product_details', args=[self.category.slug, self.slug])

  def __str__(self):
    return self.product_name