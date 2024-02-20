from rest_framework import viewsets

from comics.models import ComicMaster
from comics.serializers import ComicMasterSerializer

class ComicViewSet(viewsets.ModelViewSet):
  
    queryset = ComicMaster.objects.all()
    serializer_class = ComicMasterSerializer