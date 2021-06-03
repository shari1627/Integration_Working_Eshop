from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','short_description','more_description']
    
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' ,'phone' ,'email','password']
    
class AdminOrders(admin.ModelAdmin):
    list_display = ['product' , 'customer' ,'quantity' ,'price','firstname','lastname','phone','payment','status','address','zipcode','city','state','country','location','date']
    

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrders)