from .models import Clientes
from rest_framework import viewsets, permissions
from .serializers import ClientesSerializer


class ClientesViewset(viewsets.ModelViewSet):
    queryset=Clientes.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ClientesSerializer