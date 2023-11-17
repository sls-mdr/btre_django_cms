from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from btre.settings import EMAIL_HOST_USER
from .models import Contact


from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact


def contact(request: object) -> object:
    """
    View for handling contact form submissions.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Redirection to the listing page.

    """
    if request.method == "POST":
        # Extract form data from the POST request
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        # Check if the user is authenticated
        if request.user.is_authenticated:
            user_id = request.user.id
            # Check if the user has already made an inquiry for this listing
            has_contacted = Contact.objects.filter(
                listing_id=listing_id, user_id=user_id
            ).exists()
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing."
                )
                return redirect("/listings/" + listing_id)

        # Create a new Contact instance and save it to the database
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            realtor_email=realtor_email,
            user_id=user_id,
        )

        contact.save()

        # TODO if necessary search for gmail alternatives
        # Send email to retalor
        # send_mail(
        #     subject=f"Property Listing Inquiery: {listing}",
        #     message=f"There has been an inquiery for {listing}. Sign in into the admin panel for more info.",
        #     from_email=EMAIL_HOST_USER,
        #     recipient_list=[realtor_email, "mederersilas@gmail.com"],
        #     fail_silently=False,
        # )

        messages.success(
            request, "Your request has been submitted. A realtor will get back to you."
        )

        return redirect("/listings/" + listing_id)
    else:
        # If the request method is not POST, do nothing
        pass
