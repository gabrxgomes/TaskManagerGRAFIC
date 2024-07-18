import matplotlib
matplotlib.use('Agg')  # Configure o backend 'Agg' para evitar problemas com Tkinter

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from collections import defaultdict

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_chart(request):
    tasks = Task.objects.all()
    task_types = Task.TASK_TYPES

    # Preparar os dados para o gráfico
    task_counts = defaultdict(int)
    for task in tasks:
        task_counts[task.task_type] += 1

    labels = [label for (task_type, label) in task_types]
    sizes = [task_counts[task_type] for (task_type, label) in task_types]

    fig, ax = plt.subplots(figsize=(10, 6))  # Ajuste o tamanho do gráfico conforme necessário

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax.set_title('Distribuição das Tarefas por Tipo')

    # Converter o gráfico em uma imagem base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

    plt.close(fig)  # Fechar o gráfico para evitar sobrecarga de memória

    return render(request, 'tasks/task_chart.html', {'graphic': graphic})
