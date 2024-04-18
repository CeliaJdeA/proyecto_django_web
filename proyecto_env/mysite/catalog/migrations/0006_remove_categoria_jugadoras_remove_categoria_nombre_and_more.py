# Generated by Django 5.0.4 on 2024-04-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_posicione_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='jugadoras',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='posicione',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='posicione',
            name='status',
        ),
        migrations.AddField(
            model_name='jugadora',
            name='Categoría',
            field=models.CharField(blank=True, choices=[('pd', 'Primera División'), ('f', 'Filial'), ('i', 'Infantil'), ('c', 'Cadete'), ('a', 'Alevín')], default='c', help_text='Categoria', max_length=2),
        ),
        migrations.AddField(
            model_name='jugadora',
            name='Posición',
            field=models.CharField(blank=True, choices=[('c', 'Cierre'), ('a', 'Ala'), ('pi', 'Pivot'), ('p', 'Portera')], default='c', help_text='Posición', max_length=2),
        ),
    ]