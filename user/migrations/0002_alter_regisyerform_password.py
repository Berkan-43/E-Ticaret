# Generated by Django 4.0.6 on 2022-08-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regisyerform',
            name='password',
            field=models.IntegerField(verbose_name='Şifre'),
        ),
    ]
