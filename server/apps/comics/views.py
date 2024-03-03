from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from comics.models import ComicMaster, ComicVersion, ComicEpisode
from comics.serializers import ComicMasterSerializer, ComicVersionSerializer, ComicEpisodeSerializer
from comics.filters import ComicVersionFilter, ComicEpisodeFilter

class ComicMasterViewSet(viewsets.ModelViewSet):
  
    queryset = ComicMaster.objects.all()
    serializer_class = ComicMasterSerializer


class ComicVersionViewSet(viewsets.ModelViewSet):
  
    queryset = ComicVersion.objects.all()
    serializer_class = ComicVersionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComicVersionFilter
    
class ComicEpisodeViewSet(viewsets.ModelViewSet):
  
    queryset = ComicEpisode.objects.all()
    serializer_class = ComicEpisodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComicEpisodeFilter
    