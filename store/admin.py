from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'inventory')
    search_fields = ('title', 'sku')
    list_filter = ('category',)
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('last_update',)
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'items')
    search_fields = ('name',)

admin.site.site_header = "Store Administration"
admin.site.site_title = "Store Admin Portal"
admin.site.index_title = "Welcome to the Store Admin"