from django.shortcuts import redirect, render


def main(request):
    if request.user.is_authenticated:
        return redirect("/tasks/")
    return render(request, 'landing/landing.html')
