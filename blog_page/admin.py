from django.contrib import admin
from .models import Category, Article
# Register your models here.

# Creamos las clases para que me pueda mostrar los campos create y update que son solo de lectura en el admin djando


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ("public", 'user', 'categories__name')
    list_display = ('title','user','public','created_at', 'updated_at')# Con poner user tomamos el usuario que que creo el articulo ya que se encuentra relacionado con las llaves


    # Creamos un metodo en el cual detectamos al usuario que este creando el articulo y con ello lo guardamos en el article
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
