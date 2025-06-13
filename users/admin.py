from django.contrib import admin
from .models import Profile, Wishlist

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'state', 'country', 'phone']
    search_fields = ['user__username', 'user__email', 'phone']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date_added']
    list_filter = ['date_added']
    search_fields = ['user__username', 'product__name']
