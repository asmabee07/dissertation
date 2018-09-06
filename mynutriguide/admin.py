from django.contrib import admin


from .models import MealSelection, FoodItem, FoodQuantity, CompleteProfile

# Register your models here.

admin.site.register(CompleteProfile)
admin.site.register(MealSelection)
admin.site.register(FoodItem)
admin.site.register(FoodQuantity)