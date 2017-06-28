from . import models, serializers
from ..base.api.viewsets import CURLViewSet


class SpeakerViewset(CURLViewSet):
    queryset = models.Speaker.objects.order_by('id')
    serializer_class = serializers.SpeakerSerializer


class ConcourseViewset(CURLViewSet):
    queryset = models.Concourse.objects.order_by('id')
    serializer_class = serializers.ConcourseSerializer
