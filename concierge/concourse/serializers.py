from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Concourse, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        exclude = ('email',)


class ConcourseSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Concourse.CONCOURSE_TYPE)

    class Meta:
        model = Concourse
        exclude = ('feedback_quiz', 'registration_quiz',)
