from rest_framework import serializers

from .models import Participant, ParticipantType, TshirtSize


class ParticipantSerializer(serializers.ModelSerializer):

    kind = serializers.SlugRelatedField(allow_null=True, slug_field='kind', queryset=ParticipantType.objects.all())
    tshirt_size = serializers.SlugRelatedField(allow_null=True, slug_field='size', queryset=TshirtSize.objects.all())

    class Meta:
        model = Participant
        fields = '__all__'
