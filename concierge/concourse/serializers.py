from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Concourse, Speaker


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('id', 'first_name', 'last_name', 'email', 'about', 'created', 'modified',)


class ConcourseSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Concourse.CONCOURSE_TYPE)

    class Meta:
        model = Concourse
        fields = ('id', 'name', 'slug', 'kind', 'event', 'speaker', 'venue', 'description', 'created', 'modified',)
