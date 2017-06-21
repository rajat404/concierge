from rest_framework import serializers

from concierge.concourse.models import Concourse
from concierge.users.models import User

from .models import Participant, ParticipantType, TshirtSize


class ParticipantSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all())
    concourse = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Concourse.objects.all())
    kind = serializers.SlugRelatedField(allow_null=True, slug_field='kind', queryset=ParticipantType.objects.all())
    tshirt_size = serializers.SlugRelatedField(allow_null=True, slug_field='size', queryset=TshirtSize.objects.all())

    class Meta:
        model = Participant
        fields = '__all__'
