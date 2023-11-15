from django.shortcuts import render, redirect


def register(request):
    """A view that displays the register page"""
    if request.method == "POST":
        print("Is Submitted")
        return redirect("register")
    else:
        return render(request, "accounts/register.html")


def login(request):
    """A view that displays the login page"""
    if request.method == "POST":
        print("Is Submitted")
        return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    """A view that displays the logout page"""
    return redirect("index")


def dashboard(request):
    """A view that displays the dashboard page"""
    return render(request, "accounts/dashboard.html")
