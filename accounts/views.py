from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def register(request: object) -> object:
    """
    View for user registration.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page or redirection.

    """
    if request.method == "POST":
        # Get form values from the POST request
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if not password == password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect("register")

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken")
            return redirect("register")

        # Create a new user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        # Login user after creation and redirect to the home page
        # auth.login(request, user)
        # messages.success(request, "You are now logged in")
        # return redirect("index")

        # Display a success message and redirect to login page
        user.save()
        messages.success(request, "You are now registered and can log.")
        return redirect("login")
    else:
        # Render the registration form if the request method is not POST
        return render(request, "accounts/register.html")


def login(request: object) -> object:
    """
    View for displaying the login page and handling user login.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page or redirection.

    """
    if request.method == "POST":
        # Extract username and password from the POST request
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user using Django's authentication system
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # If authentication is successful, log in the user redirect to dashboard
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            # If authentication fails, display an error message and redirect to the login page
            messages.error(request, "Invalid credentials")
            return redirect("login")

    else:
        # If the request method is not POST, render the login form
        return render(request, "accounts/login.html")


def logout(request):
    """A view that displays the logout page"""
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect("index")


def dashboard(request):
    """A view that displays the dashboard page"""
    user_contacts = Contact.objects.order_by("-contact_date").filter(
        user_id=request.user.id
    )
    context = {"contacts": user_contacts}
    return render(request, "accounts/dashboard.html", context)
