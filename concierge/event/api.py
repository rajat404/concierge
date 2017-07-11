from concierge.base import response as rsp
from concierge.base.api.viewsets import CURLViewSet

from .models import Event, Speaker
from .serializers import EventSerializer, SpeakerSerializer
from .services import create_event


class SpeakerViewset(CURLViewSet):
    queryset = Speaker.objects.order_by('id')
    serializer_class = SpeakerSerializer


class EventViewset(CURLViewSet):
    queryset = Event.objects.order_by('id')
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        create_event(serializer)
        return rsp.Created(serializer.data)
