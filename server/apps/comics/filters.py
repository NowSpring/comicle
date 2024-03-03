import django_filters
from comics.models import ComicVersion, ComicEpisode

class ComicVersionFilter(django_filters.FilterSet):
  
    class Meta:
  
        model = ComicVersion
        fields = {
            'title_id': ['exact'],
        }

class ComicEpisodeFilter(django_filters.FilterSet):
  
    class Meta:
  
        model = ComicEpisode
        fields = {
            'title_version_id': ['exact'],
        }
