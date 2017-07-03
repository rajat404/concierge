from rest_framework import mixins, viewsets


class CURLViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """A viewset that provides `create`, `update`,
    `retrieve` and `list` (CURL) actions.

    To use it, override the class and set the
    `.queryset` and `.serializer_class` attributes.
    """
    pass
