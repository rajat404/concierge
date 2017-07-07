from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Concourse, Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('id', 'created', 'modified', 'first_name', 'last_name', 'email', 'about',)


class ConcourseSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Concourse.CONCOURSE_CHOICES)
    is_offline = serializers.BooleanField(required=True)
    participation_open = serializers.BooleanField(required=True)

    class Meta:
        model = Concourse
        fields = ('id', 'created', 'modified', 'name', 'slug', 'kind', 'event', 'speaker', 'venue', 'description',
                  'start', 'end', 'participation_open', 'participation_start', 'participation_end', 'is_offline',
                  'registration_quiz', 'feedback_quiz',)
