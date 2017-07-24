# Third Party Stuff
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Answer
from .serializers import AnswerSerializer


class AnswerViewset(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    queryset = Answer.objects.order_by('id')
    serializer_class = AnswerSerializer
