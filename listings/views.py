from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by('id').filter(is_published=True)
    paginator = Paginator(listings, 1)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    context = {
        'listings': paged_listings
    }
    print(context['listings'])
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
    if city:
        queryset_list = queryset_list.filter(city__iexact=city)
    context = {
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
