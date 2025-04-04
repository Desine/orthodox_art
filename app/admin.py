from django.contrib import admin
from .models import *


# Inline модели для Product
class ProductRelationInline(admin.TabularInline):
    extra = 1

class ProductTypeInline(ProductRelationInline):
    model = ProductType

class ProductSizeInline(ProductRelationInline):
    model = ProductSize

class ProductMaterialInline(ProductRelationInline):
    model = ProductMaterial

class ProductImageInline(ProductRelationInline):
    model = ProductImage

# Базовый класс для простых моделей
class SimpleModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# OrderProduct inline
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields = ('price_at_order',)

# Регистрация моделей
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available_amount')
    list_filter = ('available_amount',)
    search_fields = ('name',)
    inlines = [ProductTypeInline, ProductSizeInline, ProductMaterialInline, ProductImageInline]

@admin.register(Type)
class TypeAdmin(SimpleModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(SimpleModelAdmin):
    pass

@admin.register(Material)
class MaterialAdmin(SimpleModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_price', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'shipping_address')
    readonly_fields = ('order_date', 'total_price')
    inlines = [OrderProductInline]
    fieldsets = (
        (None, {'fields': ('user', 'order_date', 'total_price')}),
        ('Order Status', {'fields': ('status', 'shipping_address')}),
    )

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount')
    list_filter = ('user',)
    search_fields = ('user__username', 'product__name')

