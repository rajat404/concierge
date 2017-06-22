from concierge.base.api.mixins import CURLMixin

from . import models, serializers


class FeedbackViewset(CURLMixin):
    queryset = models.Feedback.objects.order_by('id')
    serializer_class = serializers.FeedbackSerializer
