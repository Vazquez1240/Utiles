# Generated by Django 4.2.5 on 2023-09-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utiles', '0009_alter_paquete_funcionario_delete_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='direccion_entrega',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
