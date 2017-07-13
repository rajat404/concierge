from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Event, Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('id', 'created', 'modified', 'first_name', 'last_name', 'email', 'about',)


class EventSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Event.EVENT_CHOICES)
    is_offline = serializers.BooleanField(required=True)
    participation_open = serializers.BooleanField(required=True)

    class Meta:
        model = Event
        fields = ('id', 'created', 'modified', 'name', 'slug', 'kind', 'happening', 'speaker', 'venue', 'description',
                  'start', 'end', 'participation_open', 'participation_start', 'participation_end', 'is_offline',
                  'registration_quiz', 'feedback_quiz',)

    def validate(self, data):
        _data = super().validate(data)
        start = _data.get('start')
        end = _data.get('end')
        if start > end:
            raise serializers.ValidationError("end must occur after start")
        return _data
