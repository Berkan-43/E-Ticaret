# Generated by Django 4.0.6 on 2022-08-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_registerform_email_alter_registerform_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='password',
            field=models.IntegerField(max_length=30),
        ),
    ]
