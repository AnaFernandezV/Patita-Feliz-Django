# Generated by Django 4.0.5 on 2022-06-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_carrito_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='precioSub',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
