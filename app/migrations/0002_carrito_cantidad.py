# Generated by Django 4.0.4 on 2022-06-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
