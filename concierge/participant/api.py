from . import models, serializers
from ..base.api.mixins import CURLMixin


class ParticipantViewset(CURLMixin):
    queryset = models.Participant.objects.order_by('id')
    serializer_class = serializers.ParticipantSerializer
