# Generated by Django 4.1.1 on 2022-09-26 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAPI', '0014_registro_alter_familiar_e_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinicaAPI.persona'),
        ),
    ]
