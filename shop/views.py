from django.shortcuts import render
from .models import Product
# Create your views here.

def shop_home(request):
    products = Product.objects.filter(publication_status=1)
    context={
        'title': 'Home',
        'content': 'Home',
        'product': products,
    }
    return render(request,'index.html',context)