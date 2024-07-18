from django.urls import path
from .views import add_task, task_list, task_chart

urlpatterns = [
    path('add/', add_task, name='add_task'),
    path('list/', task_list, name='task_list'),
    path('chart/', task_chart, name='task_chart'),
    
]
