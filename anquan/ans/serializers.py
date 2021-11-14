from rest_framework import serializers
from .models import An


class AnSerializer(serializers.ModelSerializer):
    #author 
    #iliked
    #i_bookmarked
    #like_count
    #parent
    #comment_count
    
    class Meta:
        model = An
        fields = '__all__'

