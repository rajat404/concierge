from . import models, serializers
from ..base.api.mixins import CURLMixin


class SpeakerViewset(CURLMixin):
    queryset = models.Speaker.objects.order_by('id')
    serializer_class = serializers.SpeakerSerializer


class ConcourseViewset(CURLMixin):
    queryset = models.Concourse.objects.order_by('id')
    serializer_class = serializers.ConcourseSerializer
