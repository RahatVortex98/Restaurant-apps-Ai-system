from django.contrib import admin
from .models import Meal,OrderTransaction

# Register your models here.
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','available',"image")
    search_fields =('name',)

@admin.register(OrderTransaction)
class OrderTransactionAdmin(admin.ModelAdmin):
    list_display = ('meal','customer','amount','status','created_at')
    search_fields = ('meal','cutomer','amount','status')