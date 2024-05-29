from rest_framework import serializers
from api.models.lapicero import Lapicero

class LapiceroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lapicero  
        fields = ['id', 'marca', 'color', 'tipo', 'material']