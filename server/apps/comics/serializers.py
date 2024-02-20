from rest_framework import serializers

from comics.models import ComicMaster


class ComicMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicMaster
        fields = "__all__"