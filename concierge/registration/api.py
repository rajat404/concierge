from concierge.base.api.mixins import CURLMixin

from . import models, serializers


class RegistrationViewset(CURLMixin):
    queryset = models.Registration.objects.order_by('id')
    serializer_class = serializers.RegistrationSerializer
