# Third Party Stuff
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewset(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):

    queryset = Participant.objects.order_by('created')
    serializer_class = ParticipantSerializer
