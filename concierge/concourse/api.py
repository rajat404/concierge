from concierge.base.api.viewsets import CURLViewSet

from .models import Concourse, Speaker
from .serializers import ConcourseSerializer, SpeakerSerializer


class SpeakerViewset(CURLViewSet):
    queryset = Speaker.objects.order_by('id')
    serializer_class = SpeakerSerializer


class ConcourseViewset(CURLViewSet):
    queryset = Concourse.objects.order_by('id')
    serializer_class = ConcourseSerializer
