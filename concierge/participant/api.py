from concierge.base.api.viewsets import CURLViewSet

from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewset(CURLViewSet):
    queryset = Participant.objects.order_by('id')
    serializer_class = ParticipantSerializer
