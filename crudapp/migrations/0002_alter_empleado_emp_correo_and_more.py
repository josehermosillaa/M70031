# Generated by Django 4.2.2 on 2023-07-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crudapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="emp_correo",
            field=models.EmailField(max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="emp_designacion",
            field=models.CharField(max_length=150, verbose_name="Designación"),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="emp_id",
            field=models.CharField(max_length=3, verbose_name="Id"),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="emp_nombre",
            field=models.CharField(max_length=200, verbose_name="Nombre"),
        ),
    ]