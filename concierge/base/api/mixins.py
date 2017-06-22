from rest_framework import mixins, viewsets


class CURLMixin(mixins.CreateModelMixin,
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


class MultiSerializerViewSetMixin(object):

    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @list_route
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        Thanks gonz: http://stackoverflow.com/a/22922156/11440
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
