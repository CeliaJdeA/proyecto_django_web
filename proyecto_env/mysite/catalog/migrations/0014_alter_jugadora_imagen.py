# Generated by Django 5.0.4 on 2024-04-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_jugadora_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadora',
            name='imagen',
            field=models.CharField(max_length=200),
        ),
    ]
