from django.contrib import admin
from .models import Stocks

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # new


admin.site.register(Stocks,StockAdmin)
