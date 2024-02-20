from django.contrib import admin

from comics.models import ComicMaster

class ComicMasterAdminConfig(admin.ModelAdmin):
  
    model = ComicMaster
    search_fields = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    list_filter = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    ordering = ('title',)
    list_display = ('title', 'author', 'era', 'publisher', 'target', 'genre',)
    fieldsets = (
        (None, {'fields': ('title', 'author', 'era', 'publisher', 'target', 'genre', 'cover', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'author', 'era', 'publisher', 'target', 'genre', 'cover', )}
         ),
    )

# Register your models here.
admin.site.register(ComicMaster, ComicMasterAdminConfig)