from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CommunityForm, CommunityTaskForm
from .models import Community, CommunityTask
from users.models import Profile
from friends.views import get_friends


User = get_user_model()


@login_required(login_url="/users/login")
def show_communities(request) -> render:
    """
    Renders the page displaying all communities belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.

    returns:
        A Django render object with context data for the "communities/communities_page.html" template.
    """
    user = request.user
    try:
        communities = user.member.all()
        context = {'communities': communities}

    except:
        context = {}
    return render(request, 'communities/communities_page.html', context)


@login_required(login_url="/users/login")
def create_community(request) -> render:
    """
    Create communities belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.

    returns:
        A Django render object with context data for the "communities/communities_page.html" template.
    """
    user = request.user
    form = CommunityForm()
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.users.add(user)
            return redirect("/communities/communities")

    context = {"form": form}
    return render(request, "communities/create_community.html", context)


@login_required(login_url="/users/login")
def update_community(request, pk) -> render:
    """
    Updates a specific task belonging to the logged-in user based on its primary key.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be updated.

    returns:
        A Django redirect object back to the tasks list page on successful update or a render object for the updated task form.
    """
    community = Community.objects.get(id=pk)
    members = community.users.all()
    form = CommunityForm(instance=community)

    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.users.add(members)

            return redirect("/communities/communities")

    context = {"form": form, "community": community}
    return render(request, "communities/update_community.html", context)


@login_required(login_url="/users/login")
def view_community(request, pk) -> render:
    """
    Renders the detailed page for a specific community belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be retrieved.

    returns:
        A Django render object with context data for the "communities/community.html" template.
    """
    community = Community.objects.get(id=pk)
    members = community.users.all()
    members = Profile.objects.filter(user__in=members)
    tasks = CommunityTask.objects.filter(community=community)
    context = {
        "community": community,
        "members": members,
        "tasks": tasks
    }
    return render(request, "communities/community.html", context)


@login_required(login_url="/users/login")
def get_member_adder(request, pk):
    user = request.user
    community = Community.objects.get(id=pk)
    friends = get_friends(request)
    members = community.users.all()
    friends_to_add = [friend for friend in friends if friend not in members]
    friends = Profile.objects.filter(user__in=friends_to_add)
    context = {
        "community": community,
        "profiles": friends
    }
    return render(request, "communities/add_member.html", context)


@login_required(login_url="/users/login")
def add_member(request, cid, uid):
    community = Community.objects.get(id=cid)
    member = User.objects.get(id=uid)
    community.users.add(member)
    return redirect("/communities/communities")


@login_required(login_url="/users/login")
def add_community_task(request, pk) -> render:
    """
    Adds a new task to the database for the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.

    returns:
        A Django redirect object back to the tasks list page on successful creation or a render object for the add task form.
    """
    community = Community.objects.get(id=pk)
    form = CommunityTaskForm()

    if request.method == "POST":
        form = CommunityTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.community = community
            form.save()
            return redirect(f"/communities/view_community/{pk}")

    context = {"form": form}
    return render(request, "tasks/add_task.html", context)


@login_required(login_url="/users/login")
def view_community_task(request, pk) -> render:
    """
    Renders the detailed page for a specific task belonging to the logged-in user.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be retrieved.

    returns:
        A Django render object with context data for the "tasks/task_view.html" template.
    """
    task = CommunityTask.objects.get(id=pk)
    context = {
        "task": task
    }
    return render(request, "tasks/task_view.html", context)


@login_required(login_url="/users/login")
def update_community_task(request, pk) -> render:
    """
    Updates a specific task belonging to the logged-in user based on its primary key.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be updated.

    returns:
        A Django redirect object back to the tasks list page on successful update or a render object for the updated task form.
    """
    task = CommunityTask.objects.get(id=pk)
    community = task.community
    form = CommunityTaskForm(instance=task)

    if request.method == "POST":
        form = CommunityTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"/communities/view_community/{community.id}")

    context = {"form": form, "community": community}
    return render(request, "communities/update_task.html", context)


@login_required(login_url="/users/login")
def delete_community_task(request, pk) -> render:
    """
    Deletes a specific task belonging to the logged-in user based on its primary key.

    params:
        request (User): The HTTP request object containing the logged-in user information.
        pk (int): The primary key of the task to be deleted.

    returns:
        A Django redirect object back to the tasks list page on successful deletion or a render object for the confirmation page.
    """
    task = CommunityTask.objects.get(id=pk)
    community = task.community

    if request.method == "POST":
        task.delete()
        return redirect(f"/communities/view_community/{community.id}")

    context = {"task": task}
    return render(request, "communities/confirm_delete.html", context)
