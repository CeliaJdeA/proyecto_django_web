# Generated by Django 5.0.4 on 2024-04-15 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_nacionalidades_nacionalidade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Jugadoras',
            new_name='Jugadora',
        ),
        migrations.RenameModel(
            old_name='Posiciones',
            new_name='Posicione',
        ),
    ]
