# Generated by Django 5.0.4 on 2024-04-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_categoria_nombre_jugadora_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadora',
            name='dorsal',
            field=models.IntegerField(default=0),
        ),
    ]