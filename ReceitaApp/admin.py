from django.contrib import admin
from django.utils.html import mark_safe
from ReceitaApp.models import Categoria, Receita

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']
    

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['nome','categoria']
    list_display_links = ['nome']
    search_fields= ['nome']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)





