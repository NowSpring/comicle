from django.contrib import admin

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode

class ReviewMasterAdminConfig(admin.ModelAdmin):
  
    model = ReviewMaster
    search_fields = ('member', 'comic_master', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_filter = ('member', 'comic_master', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_display = ('member', 'comic_master', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    ordering = ('member', 'comic_master',)
    fieldsets = (
        (None, {'fields': ('member', 'comic_master', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comic_master', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}
         ),
    )
    

class ReviewVersionAdminConfig(admin.ModelAdmin):
  
    model = ReviewVersion
    search_fields = ('member', 'comic_version', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_filter = ('member', 'comic_version', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_display = ('member', 'comic_version', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    ordering = ('member', 'comic_version',)
    fieldsets = (
        (None, {'fields': ('member', 'comic_version', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comic_version', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}
         ),
    )


class ReviewEpisodeAdminConfig(admin.ModelAdmin):
  
    model = ReviewEpisode
    search_fields = ('member', 'comic_episode', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_filter = ('member', 'comic_episode', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    list_display = ('member', 'comic_episode', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5',)
    ordering = ('member', 'comic_episode',)
    fieldsets = (
        (None, {'fields': ('member', 'comic_episode', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('member', 'comic_episode', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'comment')}
         ),
    )



admin.site.register(ReviewMaster, ReviewMasterAdminConfig)
admin.site.register(ReviewVersion, ReviewVersionAdminConfig)
admin.site.register(ReviewEpisode, ReviewEpisodeAdminConfig)