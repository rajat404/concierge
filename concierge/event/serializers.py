# Third Party Stuff
from rest_framework import serializers

# Concierge Stuff
from concierge.base.serializers import DisplayChoiceField

from .models import Event, OfflineEvent, Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('id', 'created', 'modified', 'first_name', 'last_name', 'email', 'about',)


class OfflineEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfflineEvent
        fields = ('id', 'created', 'modified', 'event', 'longitude', 'latitude', 'address', 'address_guidelines',
                  'rsvp_open', 'rsvp_start', 'rsvp_end',)


class EventSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Event.EVENT_CHOICES)
    is_offline = serializers.BooleanField(required=True)
    participation_open = serializers.BooleanField(required=True)
    offline = OfflineEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'created', 'modified', 'name', 'slug', 'kind', 'happening', 'speaker', 'venue', 'description',
                  'registration_quiz', 'feedback_quiz', 'start', 'end', 'participation_open', 'participation_start',
                  'participation_end', 'is_offline', 'offline',)

    def validate(self, data):
        data = super().validate(data)
        if data['start'] > data['end']:
            raise serializers.ValidationError('`end` must occur after `start`')
        if data['participation_open']:
            if all([data['participation_start'], data['participation_end']]) is False:
                error_dict = {'participation_open': '`participation_start` & `participation_end` also required'}
                raise serializers.ValidationError(error_dict)
        return data
