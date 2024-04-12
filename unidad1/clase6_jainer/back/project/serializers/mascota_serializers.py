from rest_framework import serializers
from api.models.mascota import Mascota

        
class MascotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mascota 
        exclude = ['id']