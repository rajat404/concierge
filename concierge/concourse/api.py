from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet

from . import models, serializers


class SpeakerViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                     UpdateModelMixin, GenericViewSet):
    queryset = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer


class ConcourseViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                       UpdateModelMixin, GenericViewSet):
    queryset = models.Concourse.objects.all()
    serializer_class = serializers.ConcourseSerializer
