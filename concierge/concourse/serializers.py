from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Concourse, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=120, allow_blank=True)
    last_name = serializers.CharField(max_length=120, allow_blank=True)
    email = serializers.EmailField()
    about = serializers.CharField()

    class Meta:
        model = Speaker
        fields = '__all__'


class ConcourseSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Concourse.CONCOURSE_TYPE)
    event = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Concourse.objects.all())
    speaker = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Speaker.objects.all())
    venue = serializers.CharField(max_length=100, allow_blank=True)

    class Meta:
        model = Concourse
        fields = '__all__'
