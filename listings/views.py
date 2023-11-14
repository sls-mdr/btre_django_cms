from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


def index(request):
    """View for the home page"""
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    page_listings = paginator.get_page(page)
    context = {"listings": page_listings}
    return render(request, "listings/listings.html", context)


def listing(request, listing_id: int):
    """View for the listing page"""
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context)


def search(request):
    """View for the search page"""
    return render(request, "listings/search.html")
