# Concierge Stuff
from concierge.base import response as rsp
from concierge.base.api.viewsets import NoDeleteModelViewSet

from .models import Event, Speaker
from .serializers import EventSerializer, SpeakerSerializer
from .services import create_event
from rest_framework.response import Response


class SpeakerViewset(NoDeleteModelViewSet):
    queryset = Speaker.objects.order_by('id')
    serializer_class = SpeakerSerializer


class EventViewset(NoDeleteModelViewSet):
    queryset = Event.objects.order_by('id')
    serializer_class = EventSerializer
    template_name = 'event_list.html'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        create_event(serializer)
        return rsp.Created(serializer.data)

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({'events': self.queryset})
        else:
            return super().list(request, *args, **kwargs)
