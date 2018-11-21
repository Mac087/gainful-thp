from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from django.http import HttpResponse
# from listings.choices import price_choices, bedroom_choices, state_choices

# from listings.models import Listing
# from realtors.models import Realtor


def index(request):
  # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

  # context = {
  #   'listings': listings,
  #   'state_choices': state_choices,
  #   'bedroom_choices': bedroom_choices,
  #   'price_choices': price_choices
  # }

  return render(request, 'page/index.html')
  #return HttpResponse('<h1>Hello World</h1>')