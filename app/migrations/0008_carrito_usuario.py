# Generated by Django 4.0.5 on 2022-06-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_carrito_esta_comprado'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]