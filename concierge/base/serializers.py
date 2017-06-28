from collections import OrderedDict

from rest_framework import serializers


class DisplayChoiceField(serializers.ChoiceField):

    def __init__(self, *args, **kwargs):
        choices = kwargs.get('choices')
        self._choices = OrderedDict(choices)
        super(DisplayChoiceField, self).__init__(*args, **kwargs)

    def to_representation(self, obj):
        """Used while retrieving value for the field."""
        return self._choices[obj]

serializers.JSONField(allow_null=False, required=True)


class MCQChoicesField(serializers.JSONField):

    def to_internal_value(self, data):
        """Set choice types to uppercase"""
        _choices = data
        for choice in _choices:
            option = _choices[choice]
            _type = option['type']
            option['type'] = _type.upper()
        data = _choices
        # super(MCQChoicesField, self).to_internal_value(data)
        return data
