from rest_framework import serializers

from .models import RegistrationAnswer, RegistrationQuiz


class RegistrationAnswerSerializer(serializers.ModelSerializer):
    is_attempted = serializers.BooleanField(required=True)

    class Meta:
        model = RegistrationAnswer
        fields = '__all__'


class RegistrationQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationQuiz
        fields = '__all__'
