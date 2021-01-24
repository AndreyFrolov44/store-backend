from django.contrib import admin

from .models import Category, Brand, Product, ProductImage, ProductSpecification, CartItem, Cart


class SpecificationInLine(admin.TabularInline):
    model = ProductSpecification


class ImageInLine(admin.TabularInline):
    model = ProductImage


class CartItemInLine(admin.TabularInline):
    model = CartItem

    def has_add_permission(self, request, obj):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'sale', 'priceSale', 'available', 'newProduct', 'topSale',)
    list_editable = ('available', 'newProduct', 'topSale',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SpecificationInLine, ImageInLine]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'address', 'order_date', 'active',)
    list_editable = ('active',)
    inlines = [CartItemInLine]

    def has_add_permission(self, request):
        return False
