from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name', 'description')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.has_perm('catalog.change_product'):
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.owner != request.user and not request.user.has_perm('catalog.change_product'):
            return ['name', 'description', 'price', 'category', 'is_published']
        return super().get_readonly_fields(request, obj)

    def has_change_permission(self, request, obj=None):
        if obj and obj.owner != request.user and not request.user.has_perm('catalog.change_product'):
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            return False
        return super().has_delete_permission(request, obj)
