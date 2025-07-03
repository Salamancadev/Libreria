from rest_framework import viewsets
from .models import ZonaRiego
from .serializer import ZonaRiegoSerializer

class ZonaRiegoViewSet(viewsets.ModelViewSet):
    queryset = ZonaRiego.objects.all()
    serializer_class = ZonaRiegoSerializer