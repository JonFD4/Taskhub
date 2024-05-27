from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task, Category
from .forms import TaskForm, CategoryForm

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
    # Retrieve all tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)

    # Filter tasks by category
    category_id = request.GET.get('category')
    if category_id:
        tasks = tasks.filter(category_id=category_id)

    # Filter tasks by priority
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)
        
    # Filter tasks by name (search)
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    return render(request, 'tasks/tasks_list.html', {'tasks': tasks, 'categories': categories})

# Category functionalities
@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Associate the current user's ID with the category
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('task_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})
@login_required
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form, 'category': category})

    #When i delete one category all of them deletes, when I add one all of them appear.
@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_list.html', {'object_type': 'Category', 'object_name': category.name})