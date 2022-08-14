# Generated by Django 4.0.6 on 2022-08-09 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_urunform_aciklama'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UrunForm2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim2', models.FileField(blank=True, null=True, upload_to='urunresmi/', verbose_name='Ürün Resmi')),
                ('fiyat2', models.IntegerField(default=0)),
                ('aciklama2', models.CharField(max_length=400, verbose_name='Açıklama')),
                ('category2', models.ManyToManyField(to='products.category2')),
                ('product2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product2')),
            ],
        ),
    ]