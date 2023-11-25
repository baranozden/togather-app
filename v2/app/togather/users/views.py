from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, ProfileForm, SignupForm
from .models import Profile


def user_signup(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/users/login")

    context = {"form": form}
    return render(request, "users/signup.html", context)


def user_login(request):
    form = LoginForm()

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
    logout(request)
    return redirect('/users/login')


@login_required(login_url="login")
def set_profile(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)
        form = ProfileForm(instance=profile)
    except:
        form = ProfileForm(instance=user)

    if request.method == "POST":
        try:
            profile = Profile.objects.get(user=user)
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        except:
            form = ProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect("/tasks/")

    context = {"form": form}
    return render(request, "users/set_profile.html", context)


@login_required(login_url="login")
def show_profile(request):
    username = request.user.username
    user = get_user_model().objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    context = {
        "user": user,
        "profile": profile
    }
    return render(request, 'users/profile_page.html', context)
