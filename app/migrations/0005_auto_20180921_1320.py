# Generated by Django 2.0.5 on 2018-09-21 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180917_1759'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chefprofile',
            unique_together={('username',)},
        ),
    ]
