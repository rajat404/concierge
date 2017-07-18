from django.core.exceptions import ImproperlyConfigured


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


class TemplateNamesMixin(object):

    def get_template_names(self):
        """
        Look for `template_names` field in the ViewSet, which
        should be a dict mapping action name (key) to template name (value),
        i.e.:

        class MyViewSet(TemplateNamesMixin, ViewSet):
            template_name = 'default.html'
            template_names = {
                'list': 'list_template.html',
                'my_action': 'my_action_template.html'
            }

            @list_route
            def my_action:
                ...

        If there's no entry for that action, then return `template_name`
        """
        if hasattr(self, 'template_names') and self.action in self.template_names:
            return [self.template_names[self.action]]
        elif hasattr(self, 'template_name'):
            return [self.template_name]
        raise ImproperlyConfigured(
            'Returned a template response with no `template_name` or '
            '`template_names` attribute set on the view'
        )
