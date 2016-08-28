from django.contrib import admin
from cart.models import Cart, ProductInCart, Order


class ProductInCartInline(admin.TabularInline):
    model = ProductInCart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    inlines = [ProductInCartInline]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("name", "phone", "email", "address", "price", "payment_type", "secret", "isAgreed", "isPaid", "isDelivered")


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)