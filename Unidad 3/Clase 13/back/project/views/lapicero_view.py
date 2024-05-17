from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.lapicero_serializers import LapiceroSerializers
from api.models.lapicero import Lapicero
from rest_framework import status
from django.http import Http404

#filtro consulta

class Lapicero_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Lapicero.objects.all()
        marca = self.request.query_params.get('marca')
        if marca is not None:
            queryset = queryset.filter(marca=marca)
        serializer = LapiceroSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = LapiceroSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Lapicero_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Lapicero.objects.get(pk=pk)
        except Lapicero.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        lapicero = self.get_object(pk)
        serializer = LapiceroSerializers(lapicero)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        lapicero = self.get_object(pk)
        serializer = LapiceroSerializers(lapicero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        lapicero = self.get_object(pk)
        lapicero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)