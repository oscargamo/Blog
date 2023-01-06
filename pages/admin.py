from django.contrib import admin

from .models import Page

# Configuracion  extra 
class PageAdmin(admin.ModelAdmin):
    readonly_fields =('created_at', 'updated_at',) # Con esto se muestran los campos que son solo de lectura en es caso se pasan los campos que se quieran mostrar
    search_fields = ('title', 'content') # Crea un buscador  diciendo que datos se quieren mostrar  en este caso se pasan dos parametros 
    list_filter = ('visible',) # Con esto se crea un filtro especificando el campo que se quiere tener 
    list_display = ('title','visible', 'created_at') # Que campos se quiere mostraran en la tabla 
    ordering = ('created_at',) # Ordena las columnas de la mas antigua a la mas reciente  podemos invertir la orden colocando -created_at


# Register your models here.
admin.site.register(Page, PageAdmin)


# configuracion del panel de gestion
title = "Panel de Gestion"
subtitle = "Panel de Gestion"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
