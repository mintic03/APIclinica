# Generated by Django 4.1.1 on 2022-09-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAPI', '0004_alter_paciente_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='latitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='longitud',
            field=models.FloatField(),
        ),
    ]
