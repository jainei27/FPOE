from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.mascota import Mascota
from ..serializers.mascota_serializers import MascotaSerializers

from rest_framework import status
from django.http import Http404

class Mascota_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        mascota = Mascota.objects.all()
        serializer = MascotaSerializers(mascota, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MascotaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Mascota_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        mascota = self.get_object(pk)
        serializer = MascotaSerializers(mascota)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        mascota = self.get_object(pk)
        serializer = MascotaSerializers(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)