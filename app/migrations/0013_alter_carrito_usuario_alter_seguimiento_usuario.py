# Generated by Django 4.0.5 on 2022-06-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_estadopedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='usuario',
            field=models.IntegerField(default=0),
        ),
    ]
