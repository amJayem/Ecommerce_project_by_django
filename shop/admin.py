from django.contrib import admin

# Register your models here.

from .models import Category, Manufacturer, Product
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

class ProductModel(admin.ModelAdmin):
    list_display = ['name', 'image' , 'publication_status','price']
    list_display_links = ['name']
    list_filter = ['publication_status']
    search_fields = ['name','price']
    
    class Meta:
        model = Product

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product,ProductModel)