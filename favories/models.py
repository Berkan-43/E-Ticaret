from django.db import models

# Create your models here.
class Urunler(models.Model):
    gorsel = models.ImageField(upload_to='resim/', null=True, blank=True, verbose_name='Ürün Resmi')
    ucret = models.IntegerField(default=0, verbose_name='Ücret')
    hakkinda =  models.TextField(max_length=400, verbose_name='Açıklama')

    def __str__(self):
        return self.hakkinda



