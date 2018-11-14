from rest_framework import routers, serializers, viewsets

from models import ModeloUno

class ModeloUnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModeloUno
        fields = ('nombre',)

# ViewSets define the view behavior.
class ModeloUnoViewSet(viewsets.ModelViewSet):
    queryset = ModeloUno.objects.all()
    serializer_class = ModeloUnoSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'modelo-uno', ModeloUnoViewSet)
