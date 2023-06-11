from django.contrib import admin

from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'email',
                    'gender', 'phone', 'avatar')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Category)
admin.site.register(Gender)

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')