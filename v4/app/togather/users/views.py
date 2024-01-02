from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, ProfileForm, SignupForm
from .models import Profile


def user_signup(request) -> render:
    """
    Registers a new user based on the provided information in the signup form.

    params:
        request (HttpRequest): The HTTP request object containing user input.

    returns:
        A Django redirect object back to the login page on successful signup or a render object for the signup form.
    """
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


def user_login(request) -> render:
    """
    Logs a user in based on the provided credentials in the login form.

    params:
        request (HttpRequest): The HTTP request object containing user input.

    returns:
        A Django redirect object to the tasks page for existing users or the profile setup page for new users,
        or a render object for the login form.
    """
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
def user_logout(request) -> redirect:
    """
    Logs out the currently logged-in user and redirects them to the login page.

    params:
        request (HttpRequest): The HTTP request object.

    returns:
        A Django redirect object back to the login page.
    """
    logout(request)
    return redirect('/users/login')


@login_required(login_url="login")
def set_profile(request) -> render:
    """
    Allows the user to create or update their profile information.

    params:
        request (HttpRequest): The HTTP request object containing user data.

    returns:
        A Django redirect object back to the tasks page on successful profile update or a render object for the profile form.
    """
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
def show_profile(request) -> render:
    """
    Displays the profile information of the currently logged-in user.

    params:
        request (HttpRequest): The HTTP request object.

    returns:
        A Django render object with context data for the profile_page.html template.
    """
    username = request.user.username
    user = get_user_model().objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        "user": user,
        "profile": profile
    }
    return render(request, 'users/profile_page.html', context)
