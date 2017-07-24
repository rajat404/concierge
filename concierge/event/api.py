# Third Party Stuff
from rest_framework import mixins
# from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Concierge Stuff
from concierge.base import response as rsp
from concierge.base.api.mixins import TemplateNamesMixin

from .models import Event, OfflineEvent, Speaker
from .serializers import EventSerializer, OfflineEventSerializer, SpeakerSerializer
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
                   TemplateNamesMixin,
                   GenericViewSet):

    queryset = Event.objects.order_by('start')
    serializer_class = EventSerializer
    template_name = 'event/list.html'
    template_names = {
        'list': 'event/list.html',
        'retrieve': 'event/detail.html',
    }

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
