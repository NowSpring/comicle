from rest_framework import viewsets

from comics.models import ComicMaster, ComicVersion, ComicEpisode
from comics.serializers import ComicMasterSerializer, ComicVersionSerializer, ComicEpisodeSerializer

class ComicMasterViewSet(viewsets.ModelViewSet):
  
    queryset = ComicMaster.objects.all()
    serializer_class = ComicMasterSerializer


class ComicVersionViewSet(viewsets.ModelViewSet):
  
    queryset = ComicVersion.objects.all()
    serializer_class = ComicVersionSerializer
    
    
class ComicEpisodeViewSet(viewsets.ModelViewSet):
  
    queryset = ComicEpisode.objects.all()
    serializer_class = ComicEpisodeSerializer