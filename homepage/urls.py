from django.contrib import admin
from django.urls import path
from soothestore.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('FindProduct/', SearchPage),
    path('Buy/<int:product_id>/', Buy),
    path('FAQ/', FAQ),
    path('Cart/', Cart),
    path('VerifyCart/', CheckCart.as_view()),
]