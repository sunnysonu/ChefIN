# Generated by Django 2.0.5 on 2018-10-08 08:40

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180921_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefprofile',
            name='dishes',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1100, size=10),
        ),
    ]
