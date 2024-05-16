from rest_framework import serializers
from api.models.lapicero import Lapicero

class LapiceroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lapicero  
        exclude = ['id']