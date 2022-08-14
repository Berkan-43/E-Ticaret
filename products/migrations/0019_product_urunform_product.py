# Generated by Django 4.0.6 on 2022-08-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_category_urunform_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='urunform',
            name='product',
            field=models.ManyToManyField(null=True, to='products.product'),
        ),
    ]