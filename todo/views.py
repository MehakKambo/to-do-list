from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.
# Uses the task_list.html
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
# Uses the task_detail.html
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'