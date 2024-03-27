from rest_framework import serializers
from api.models import Post
from api.models import Lapicero

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']

class LapiceroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lapicero  
        exclude = ['id']