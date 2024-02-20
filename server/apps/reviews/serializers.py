from rest_framework import serializers

from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode

class ReviewMasterSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ReviewMaster
        fields = "__all__"


class ReviewVersionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ReviewVersion
        fields = "__all__"


class ReviewEpisodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = ReviewEpisode
        fields = "__all__"