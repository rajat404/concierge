# Third Party Stuff
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Concierge Stuff
from concierge.base import response as rsp

from .models import Speaker, Event, OfflineEvent
from .serializers import SpeakerSerializer, EventSerializer, OfflineEventSerializer
from .services import create_event


class SpeakerViewset(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):

    queryset = Speaker.objects.order_by('id')
    serializer_class = SpeakerSerializer


class EventViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Event.objects.order_by('start')
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        create_event(serializer)
        return rsp.Created(serializer.data)


class OfflineEventViewset(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):

    queryset = OfflineEvent.objects.order_by('id')
    serializer_class = OfflineEventSerializer
