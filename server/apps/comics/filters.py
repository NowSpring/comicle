import django_filters
from comics.models import ComicVersion

class ComicVersionFilter(django_filters.FilterSet):
  
    class Meta:
  
        model = ComicVersion
        fields = {
            'title_id': ['exact'],
        }
