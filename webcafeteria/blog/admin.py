from django.contrib import admin
from .models import Category, post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    list_display=('title', 'author', 'published', 'post_categorie')
    ordering= ('author', 'published')
    search_fields=('title', 'author__username')
    date_hierarchy='published'
    list_filter= ('categories__name','author__username')

    def post_categorie(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categorie.short_description='Categoria'

admin.site.register(Category, CategoryAdmin)
admin.site.register(post, PostAdmin)