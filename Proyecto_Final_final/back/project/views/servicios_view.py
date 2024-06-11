from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.servicios_serializers import ServiciosSerializers
from api.models.servicios import Servicios
from rest_framework import status
from django.http import Http404


class Servicios_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Servicios.objects.all()
        cedula = self.request.query_params.get('cedula')
        if cedula is not None:
            queryset = queryset.filter(cedula = cedula)
        serializer = ServiciosSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ServiciosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Servicios_APIView_Detail(APIView):
    def get_object(self, pk):
        try:

            return Servicios.objects.get(pk=pk)
        except Servicios.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        servicios = self.get_object(pk)
        serializer = ServiciosSerializers(servicios)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        servicios = self.get_object(pk)
        serializer = ServiciosSerializers(servicios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        servicios = self.get_object(pk)
        servicios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)