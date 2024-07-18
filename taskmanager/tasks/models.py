from django.db import models

class Task(models.Model):
    TASK_TYPES = [
        ('installation', 'Instalação'),
        ('maintenance', 'Manutenção'),
        ('management', 'Gestão'),
        ('inspection', 'Vistoria'),
        ('site_maintenance', 'Manutenção do site'),
        ('site_implementation', 'Implementação no site'),
        ('service_order_creation', 'Criação de ordem de serviço'),
        ('employee_management', 'Gestão de funcionários'),
    ]
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_task_type_display()} - {self.created_at}'
