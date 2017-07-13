from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class NoDeleteModelViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """A viewset that provides `create`, `update` (and `partial_update`),
    `retrieve` and `list` (CURL) actions.

    Essentially it's `ModelViewSet` without the `delete` action
    """
    pass
