from django.contrib import admin
from .models import CategoriaP, Producto

class Prodamin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class Productoadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(CategoriaP, Prodamin)

admin.site.register(Producto, Productoadmin)

