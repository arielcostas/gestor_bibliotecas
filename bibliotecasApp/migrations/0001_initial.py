# Generated by Django 4.1.1 on 2022-11-04 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.CharField(max_length=50)),
                ('idioma', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('dni', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecasApp.libro')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecasApp.socio')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
            },
        ),
    ]