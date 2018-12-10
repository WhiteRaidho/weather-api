from measurements.models import Temperature, Config
from rest_framework import serializers

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('value', 'date', 'name')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('name', 'mac', 'enabled')
