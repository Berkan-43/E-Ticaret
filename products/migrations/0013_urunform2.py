# Generated by Django 4.0.6 on 2022-08-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_urunform_fiyat'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrunForm2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='urunpicture/', verbose_name='Ürün Resmi')),
                ('fee', models.DecimalField(decimal_places=100, max_digits=500000)),
                ('explanation', models.TextField(max_length=400, verbose_name='Açıklama')),
            ],
        ),
    ]