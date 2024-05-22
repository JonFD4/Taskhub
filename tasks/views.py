from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm

@login_required
def create_task(request):
    # Handle creation of a new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def read_task(request, pk):
    # Retrieve details of a specific task. Displayed in task_details
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        return HttpResponseForbidden()
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, pk):
    # Handle deletion of an existing task
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task_confirmation.html', {'task': task})

@login_required
def task_list(request):
    # Retrieve all tasks for the logged-in user. Dashboard
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})
