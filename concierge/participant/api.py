from . import models, serializers
from ..base.api.viewsets import CURLViewSet


class ParticipantViewset(CURLViewSet):
    queryset = models.Participant.objects.order_by('id')
    serializer_class = serializers.ParticipantSerializer
