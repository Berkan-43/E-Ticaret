# Generated by Django 4.0.6 on 2022-08-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_registerform_owner_registerform_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
    ]