from audioop import reverse
from distutils.command import upload
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  category_name = models.CharField('Categoría', max_length=30, unique=True)
  description = models.CharField('Descripción', max_length=255, blank=True)
  slug = models.CharField(max_length=100, unique=True)
  cat_image = models.ImageField('Imagen', upload_to='photos/categories', blank=True)

  class Meta:
    verbose_name = 'categoría'
    verbose_name_plural = 'categorías'

  def get_url(self):
    return reverse('products_by_category', args=[self.slug])

  def __str__(self):
    return self.category_name