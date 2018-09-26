from django.contrib import admin

# Register your models here.

from .models import Item, WishList

admin.site.register((Item, WishList))
