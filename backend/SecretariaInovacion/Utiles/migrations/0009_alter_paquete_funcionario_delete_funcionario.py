# Generated by Django 4.2.5 on 2023-09-26 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios_app', '0001_initial'),
        ('Utiles', '0008_paquete_entregado_paquete_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='funcionarios_app.funcionario'),
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
