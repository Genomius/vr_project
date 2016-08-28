from django.contrib import admin
from models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("title", "preview_image_url", "price", "in_stoke_count", "sales_count")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Product, ProductAdmin)
