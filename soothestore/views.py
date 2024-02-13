from django.shortcuts import render
from algoliasearch_django import raw_search
from .models import MassageChair
from rest_framework.response import Response
from .models import MassageChair
from .serializers import MassageChairSerializer
import json

def extract_product_data(algolia_data):

   extracted_data = {
       "title": algolia_data["title"],
       "price": algolia_data["price"],
       "description": algolia_data["description"],
       "brand": algolia_data["brand"],
       "available_colors": algolia_data["color_options"],
       "features": algolia_data["chair_features"],
       "purchased": algolia_data["purchased"],
       "rating": algolia_data["rating"],
       "posted": algolia_data["posted"],
   }
   return extracted_data

def HomePage(request):
    response = raw_search(MassageChair, "osaki")['hits'][0]
    if response:
        product_details = extract_product_data(response)
    return render(request, 'homePage-design/home.html')

def SearchPage(request):
    return render(request, 'homePage-design/searchPage.html')

def Buy(request, product_id):
    return render(request, 'homePage-design/Buy.html')

def FAQ(request):
    return render(request, 'homePage-design/FAQ.html')

def Cart(request):
    return render(request, 'homePage-design/finalcart.html')

def CheckCart(request):
    def get(self, request, *args, **kwargs):
        product_ids = json.loads(request.body) if request.body else []
        # massage_chairs = MassageChair.objects.filter(id__in=product_ids)
        # serializer = MassageChairSerializer(massage_chairs, many=True)
        return Response({'true':'true'})