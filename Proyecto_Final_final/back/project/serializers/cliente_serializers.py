from rest_framework import serializers
from api.models.cliente import Cliente

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente

        fields = ['id','nombre','apellido','cedula','telefono','correo']
