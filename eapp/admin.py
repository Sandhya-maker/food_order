from django.contrib import admin
from eapp.models import categories,food_items,food_variants
# Register your models here.

class food_items_admin(admin.ModelAdmin):
    list_display = ["name", "img", "category"]
class food_variants_admin(admin.ModelAdmin):
    list_display = ["name", "food", "price"]
admin.site.register(categories)
admin.site.register(food_items,  food_items_admin)
admin.site.register(food_variants, food_variants_admin)