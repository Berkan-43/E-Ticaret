from itertools import product
from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class UrunForm(models.Model):
    category = models.ManyToManyField('category')
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    resim = models.ImageField(upload_to='urunresmi/', null=True, blank=True, verbose_name='Ürün Resmi')
    fiyat = models.IntegerField(default=0)
    aciklama = models.CharField(max_length=400, verbose_name='Açıklama')

    def __str__(self):
            return self.aciklama
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



