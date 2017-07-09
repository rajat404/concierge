from rest_framework import viewsets

from .. import exceptions as exc


class CURLViewSet(viewsets.ModelViewSet):
    """A viewset that provides `create`, `partial_update`,
    `retrieve` and `list` (CURL) actions.

    To use it, override the class and set the
    `.queryset` and `.serializer_class` attributes.
    """

    def update(self, request, pk=None):
        raise exc.NotSupported

    def destroy(self, request, pk=None):
        raise exc.NotSupported
