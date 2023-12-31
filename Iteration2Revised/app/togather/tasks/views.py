from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


@login_required(login_url="/users/login")
def show_tasks(request):
    """Show tasks belonging to the related user"""
    user = request.user
    try:
        tasks = Task.objects.filter(user=user)
        context = {'tasks': tasks}
    except:
        context = {}
    return render(request, 'tasks/tasks_page.html', context)


@login_required(login_url="/users/login")
def add_task(request):
    """Add task to the db wrt creator user"""
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("/tasks/")

    context = {"form": form}
    return render(request, "tasks/add_task.html", context)


@login_required(login_url="/users/login")
def update_task(request, pk):
    """Update selected (wrt primary key) task"""
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")

    context = {"form": form}
    return render(request, "tasks/update_task.html", context)


@login_required(login_url="/users/login")
def delete_task(request, pk):
    """Delete selected (wrt primary key) task"""
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/tasks/")

    context = {"task_name": task.task_name}
    return render(request, "tasks/confirm_delete.html", context)
