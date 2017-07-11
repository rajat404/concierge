from rest_framework import serializers

from concierge.event.models import Event

from .models import Participant, ParticipantType, TshirtSize


class ParticipantSerializer(serializers.ModelSerializer):

    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    kind = serializers.SlugRelatedField(allow_null=False, slug_field='kind', queryset=ParticipantType.objects.all())
    tshirt_size = serializers.SlugRelatedField(allow_null=False, slug_field='size', queryset=TshirtSize.objects.all())

    class Meta:
        model = Participant
        fields = ('id', 'user', 'event', 'kind', 'tshirt_size', 'created', 'modified',)

    def validate_event(self, event):
        participation_open = event.participation_open
        can_participate = event.can_participate()

        if all([participation_open, can_participate]) is False:
            raise serializers.ValidationError('Registrations are closed for this event.')
        return event
