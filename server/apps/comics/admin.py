from django.contrib import admin

from comics.models import ComicMaster, ComicVersion

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


class ComicVersionAdminConfig(admin.ModelAdmin):
  
    model = ComicVersion
    search_fields = ('title', 'version_number',)
    list_filter = ('title', 'version_number',)
    ordering = ('title',)
    list_display = ('title', 'version_number',)
    fieldsets = (
        (None, {'fields': ('title', 'version_number', 'cover',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'version_number', 'cover',)}
         ),
    )


admin.site.register(ComicMaster, ComicMasterAdminConfig)
admin.site.register(ComicVersion, ComicVersionAdminConfig)