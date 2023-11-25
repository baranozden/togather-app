from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, ProfileForm, SignupForm
from .models import Profile


def user_signup(request):
    """Signs user up wrt request content"""
    form = SignupForm()

    # when a post request received use the content
    # and save the user's credentials to db
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users/login")

    context = {"form": form}
    return render(request, "users/signup.html", context)


def user_login(request):
    """Logs user in wrt request content"""
    form = LoginForm()

    # when a post request received use the content
    # and authenticate the user
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                if Profile.objects.filter(user=user).exists():
                    return redirect("/tasks/")
                else:
                    return redirect("/users/set_profile")

    context = {"form": form}
    return render(request, 'users/login.html', context)


@login_required(login_url="login")
def user_logout(request):
    """Logs out related user"""
    logout(request)
    return redirect('/users/login')


@login_required(login_url="login")
def set_profile(request):
    """Update or create profile for user"""
    user = request.user
    form = ProfileForm()

    # when a post request received use the content
    # and create or update user profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        # if user profile already exists, inherit that profile and update
        # if profile does not exist create
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form.instance.user = request.user

        if form.is_valid():
            form.save()
        return redirect("/tasks/")

    context = {"form": form}
    return render(request, "users/set_profile.html", context)


@login_required(login_url="login")
def show_profile(request):
    """Show profile of the related user"""
    username = request.user.username
    user = get_user_model().objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        "user": user,
        "profile": profile
    }
    return render(request, 'users/profile_page.html', context)
