from rest_framework import viewsets
from measurements.models import Temperature, Config
from .serializers import TemperatureSerializer, ConfigSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters

class TemperatureFilter(filters.FilterSet):
    class Meta:
        model = Temperature
        fields =    {
            'value' :['iexact','lte','gte'],
            'name': ['icontains'],
            'date' : ['iexact','lte','gte'],
        }

class ConfigFilter(filters.FilterSet):
    class Meta:
        model = Config
        fields = {
            'mac' : ['iexact'],
            'enabled' : ['iexact'],
            'name' : ['iexact'],
        }

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filterset_class = TemperatureFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    filterset_class = ConfigFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
