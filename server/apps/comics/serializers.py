from rest_framework import serializers

from comics.models import ComicMaster, ComicVersion, ComicEpisode


class ComicMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicMaster
        fields = "__all__"
       
        
class ComicVersionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicVersion
        fields = "__all__"
        

class ComicEpisodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ComicEpisode
        fields = "__all__"