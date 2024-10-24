from django.contrib import admin
from .models import ProductCategory, ProductSubCategory, Product , shipping_address

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_category_name', 'product_category_image']
    search_fields = ['product_category_name']


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_sub_category_name', 'product_category', 'product_sub_category_image']
    search_fields = ['product_sub_category_name']
    list_filter = ['product_category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_category', 'product_sub_category', 'product_price', 'product_listing_time']
    search_fields = ['product_name']
    list_filter = ['product_category', 'product_sub_category']


admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ProductSubCategory,ProductSubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(shipping_address)