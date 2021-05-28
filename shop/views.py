from django.shortcuts import render

# Create your views here.

def shop_home(request):
    
    context={
        'title': 'Home',
        'content': 'Home'
    }
    return render(request,'index.html',context)