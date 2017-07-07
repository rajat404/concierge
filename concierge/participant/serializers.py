from rest_framework import serializers

from concierge.concourse.models import Concourse

from .models import Participant, ParticipantType, TshirtSize


class ParticipantSerializer(serializers.ModelSerializer):

    concourse = serializers.PrimaryKeyRelatedField(queryset=Concourse.objects.all())
    kind = serializers.SlugRelatedField(allow_null=False, slug_field='kind', queryset=ParticipantType.objects.all())
    tshirt_size = serializers.SlugRelatedField(allow_null=False, slug_field='size', queryset=TshirtSize.objects.all())

    class Meta:
        model = Participant
        fields = ('id', 'user', 'concourse', 'kind', 'tshirt_size', 'created', 'modified',)

    def validate_concourse(self, concourse):
        participation_open = concourse.participation_open
        can_participate = concourse.can_participate()

        if all([participation_open, can_participate]) is False:
            raise serializers.ValidationError('Registrations are closed for this event.')
        return concourse
