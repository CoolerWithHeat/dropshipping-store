from django.shortcuts import render
from algoliasearch_django import raw_search
from .models import MassageChair
from rest_framework.response import Response
from rest_framework.views import APIView
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

class CheckCart(APIView):
    def post(self, request, *args, **kwargs):
        products = json.loads(request.body) if request.body else []
        total_price = 0
        verified_cart = []
        try:
            product_ids = [product['product_id'] for product in products]
            verified_products = MassageChair.objects.filter(id__in=product_ids)
            for each in verified_products:
                desired_product_id = each.id
                desired_product = next((product for product in products if product['product_id'] == desired_product_id), None)
                product_object = {}
                if desired_product:
                    product_object['id'] = each.id
                    product_object['title'] = each.title    
                    product_object['quantity'] = desired_product['quantity']
                    product_object['price'] = each.price
                    total_price += (each.price * desired_product['quantity'])
                    images = each.available_colors.all()
                    if images:
                        image_url = images[0].image.url
                        color = str(images[0])
                        product_object['color'] = color
                        product_object['image'] = image_url
                    verified_cart.append(product_object)
        except:
            pass
        
        return Response({'cart': verified_cart, 'total_price': total_price, 'verified_products':len(verified_cart)}, status=200)