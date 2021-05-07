from django.contrib import admin
from .models import CategoryModel

# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    fields = ['cat_name','cat_image','is_active']


admin.site.register(CategoryModel, CategoryModelAdmin)