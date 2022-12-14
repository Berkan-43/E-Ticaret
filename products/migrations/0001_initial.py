# Generated by Django 4.0.6 on 2022-08-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrunForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.FileField(blank=True, null=True, upload_to='urunresmi/', verbose_name='Ürün Resmi')),
                ('fiyat', models.IntegerField(default=0)),
                ('aciklama', models.TextField(max_length=400, verbose_name='Açıklama')),
            ],
        ),
    ]
