from measurements.api.viewsets import TemperatureViewSet, ConfigViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('temperature', TemperatureViewSet, base_name='temperature')
router.register('config', ConfigViewSet, base_name='config')
