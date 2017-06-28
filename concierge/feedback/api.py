from concierge.base.api.viewsets import CURLViewSet

from . import models, serializers


class FeedbackViewset(CURLViewSet):
    queryset = models.Feedback.objects.order_by('id')
    serializer_class = serializers.FeedbackSerializer
