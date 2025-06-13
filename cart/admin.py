from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'user', 'date_added']
    search_fields = ['cart_id', 'user__username']
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'sub_total']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'email', 'phone', 'order_total', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered', 'created_at']
    search_fields = ['order_number', 'first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['order_number', 'order_total', 'ip']
    inlines = [OrderItemInline]
    list_per_page = 20
