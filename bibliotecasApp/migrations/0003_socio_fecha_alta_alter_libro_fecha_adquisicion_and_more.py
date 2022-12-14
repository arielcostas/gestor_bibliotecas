# Generated by Django 4.1.3 on 2022-11-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecasApp', '0002_alter_socio_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='fecha_alta',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_adquisicion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
