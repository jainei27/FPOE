from rest_framework import serializers
from back.api.models.lapicero import Lapicero

class LapiceroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lapicero  
        exclude = ['id']