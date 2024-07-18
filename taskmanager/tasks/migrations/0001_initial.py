# Generated by Django 5.0.7 on 2024-07-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('installation', 'Instalação'), ('maintenance', 'Manutenção'), ('management', 'Gestão'), ('inspection', 'Vistoria'), ('site_maintenance', 'Manutenção do site'), ('site_implementation', 'Implementação no site'), ('service_order_creation', 'Criação de ordem de serviço'), ('employee_management', 'Gestão de funcionários')], max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
