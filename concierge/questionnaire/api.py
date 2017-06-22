from concierge.base.api.mixins import CURLMixin

from . import models, serializers


class QuestionnaireViewset(CURLMixin):
    queryset = models.Questionnaire.objects.order_by('id')
    serializer_class = serializers.QuestionnaireSerializer
