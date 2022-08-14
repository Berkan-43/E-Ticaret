# Generated by Django 4.0.6 on 2022-08-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_rename_password_registerform_password1'),
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