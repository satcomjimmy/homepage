from django.contrib import admin

from .models import Grocery, Meal

# Register your models here.
admin.site.register(Grocery)
admin.site.register(Meal)