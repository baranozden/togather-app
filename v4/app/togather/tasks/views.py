from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


@login_required(login_url="/users/login")
def show_tasks(request) -> render:
    """
    Renders the page displaying all tasks belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.

    returns:
        A Django render object with context data for the "tasks/tasks_page.html" template.
    """
    user = request.user
    try:
        tasks = Task.objects.filter(user=user)
        context = {'tasks': tasks}
    except:
        context = {}
    return render(request, 'tasks/tasks_page.html', context)


def view_task(request, pk) -> render:
    """
    Renders the detailed page for a specific task belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be retrieved.

    returns:
        A Django render object with context data for the "tasks/task_view.html" template.
    """
    task = Task.objects.get(id=pk)
    context = {
        "task": task
    }
    return render(request, "tasks/task_view.html", context)


@login_required(login_url="/users/login")
def add_task(request) -> render:
    """
    Adds a new task to the database for the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.

    returns:
        A Django redirect object back to the tasks list page on successful creation or a render object for the add task form.
    """
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
def update_task(request, pk) -> render:
    """
    Updates a specific task belonging to the logged-in user based on its primary key.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be updated.

    returns:
        A Django redirect object back to the tasks list page on successful update or a render object for the updated task form.
    """
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
def delete_task(request, pk) -> render:
    """
    Deletes a specific task belonging to the logged-in user based on its primary key.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be deleted.

    returns:
        A Django redirect object back to the tasks list page on successful deletion or a render object for the confirmation page.
    """
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/tasks/")

    context = {"task_name": task.task_name}
    return render(request, "tasks/confirm_delete.html", context)
