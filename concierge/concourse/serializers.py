from django.utils import timezone
from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField
from concierge.quiz.models import Quiz

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

    # def validate(self, data):
    #     data = super().validate(data)
    #     end = data.get('end')
    #     participation_open = data.get('participation_open')
    #     participation_start = data.get('participation_start')
    #     participation_end = data.get('participation_end')

    #     if participation_open:
    #         # If `participation_start` is not given,
    #         # then it's set to current datetime
    #         if participation_start in ('', None):
    #             participation_start = timezone.now()
    #         # If `participation_end` is not given,
    #         # then it's set to current datetime
    #         if participation_end in ('', None):
    #             participation_end = end

    #     data['participation_start'] = participation_start
    #     data['participation_end'] = participation_end
    #     return data
