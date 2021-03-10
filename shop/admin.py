from django.contrib import admin

from .models import *

class InlineProductOrder(admin.TabularInline):
    model = ProductOrder

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):    
    inlines = (InlineProductOrder,)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (InlineProductOrder,)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):    
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):    
    pass