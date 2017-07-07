from concierge.base import response as rsp
from concierge.base.api.viewsets import CURLViewSet

from .models import Concourse, Speaker
from .serializers import ConcourseSerializer, SpeakerSerializer
from .services import create_concourse


class SpeakerViewset(CURLViewSet):
    queryset = Speaker.objects.order_by('id')
    serializer_class = SpeakerSerializer


class ConcourseViewset(CURLViewSet):
    queryset = Concourse.objects.order_by('id')
    serializer_class = ConcourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        create_concourse(serializer)
        return rsp.Created(serializer.data)
