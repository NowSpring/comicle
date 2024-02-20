from rest_framework import viewsets

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode
from reviews.serializers import ReviewMasterSerializer, ReviewVersionSerializer, ReviewEpisodeSerializer


class ReviewMasterViewSet(viewsets.ModelViewSet):
  
    queryset = ReviewMaster.objects.all()
    serializer_class = ReviewMasterSerializer


class ReviewVersionViewSet(viewsets.ModelViewSet):
  
    queryset = ReviewVersion.objects.all()
    serializer_class = ReviewVersionSerializer
    

class ReviewEpisodeViewSet(viewsets.ModelViewSet):
  
    queryset = ReviewEpisode.objects.all()
    serializer_class = ReviewEpisodeSerializer