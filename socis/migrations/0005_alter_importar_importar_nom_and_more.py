# Generated by Django 4.2.2 on 2023-06-25 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socis', '0004_alter_importar_importar_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importar',
            name='importar_nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='importar',
            name='importar_ruta',
            field=models.FileField(upload_to='arxius', verbose_name='Csv'),
        ),
    ]
