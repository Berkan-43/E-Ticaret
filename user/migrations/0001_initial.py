# Generated by Django 4.0.6 on 2022-08-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisyerForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='İsim-Soyisim')),
                ('email', models.TextField(max_length=30, verbose_name='E-mail')),
                ('password', models.IntegerField(max_length=100, verbose_name='Şifre')),
            ],
        ),
    ]
