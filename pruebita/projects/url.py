from rest_framework import routers
from .api import ClientesViewset
router=routers.DefaultRouter()

router.register('api/Clientes', ClientesViewset,'Clientes')
urlpatterns=router.urls