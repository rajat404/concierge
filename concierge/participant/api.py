from concierge.base.api.viewsets import NoDeleteModelViewSet

from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewset(NoDeleteModelViewSet):
    queryset = Participant.objects.order_by('created')
    serializer_class = ParticipantSerializer
