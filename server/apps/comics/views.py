from rest_framework import viewsets

from comics.models import ComicMaster, ComicVersion
from comics.serializers import ComicMasterSerializer, ComicVersionSerializer

class ComicMasterViewSet(viewsets.ModelViewSet):
  
    queryset = ComicMaster.objects.all()
    serializer_class = ComicMasterSerializer


class ComicVersionViewSet(viewsets.ModelViewSet):
  
    queryset = ComicVersion.objects.all()
    serializer_class = ComicVersionSerializer