from .models import CarShowroom
from rest_framework import viewsets, mixins
from .serializers import CarShowroomSerializer


class CarShowroomListViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = CarShowroomSerializer
    queryset = CarShowroom.objects.all()
