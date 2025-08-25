from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')
    list_filter = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(client=request.user.client)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('name', 'stock', 'price', 'client')
        return ('name', 'stock', 'price')

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ('client',)
        return ()

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        return [(None, {'fields': ('name', 'stock', 'price')})]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "client" and not request.user.is_superuser:
            kwargs["queryset"] = request.user.client.__class__.objects.filter(pk=request.user.client.pk)
            kwargs["initial"] = request.user.client
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.client:
            obj.client = request.user.client
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
