# Generated by Django 4.2.2 on 2023-06-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socis', '0003_importar_importar_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importar',
            name='importar_nom',
            field=models.FileField(upload_to='soc', verbose_name='Csv'),
        ),
    ]