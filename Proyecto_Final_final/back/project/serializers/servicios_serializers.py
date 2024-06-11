from rest_framework import serializers
from api.models.servicios import Servicios

class ServiciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios

        fields = ['id','nombre','cedula','descripcion','valor']
