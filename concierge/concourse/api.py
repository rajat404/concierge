from . import models, serializers
from ..base.api.viewsets import CURLViewSet


class SpeakerViewset(CURLViewSet):
    queryset = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer


class ConcourseViewset(CURLViewSet):
    queryset = models.Concourse.objects.all()
    serializer_class = serializers.ConcourseSerializer
