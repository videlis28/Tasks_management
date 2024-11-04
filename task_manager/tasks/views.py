from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        name = request.POST['task']
        Task.objects.create(name=name)
        return redirect('index')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.name = request.POST['task']
        task.save()
        return redirect('index')
    return render(request, 'edit_task.html', {'task': task})
