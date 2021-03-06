# Third Party Imports
from rest_framework import serializers

# Concierge Imports
from concierge.quiz.models import Question

from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ('id', 'question', 'text_answer', 'choice_answer', 'participant', 'created', 'modified',)

    def validate(self, data):
        _data = super().validate(data)
        question_obj = _data.get('question')
        text_answer = _data.get('text_answer')
        choice_answer = _data.get('choice_answer')

        required = question_obj.required
        kind = question_obj.kind
        editable = question_obj.editable

        if required:
            if kind == 'MCQ' and not choice_answer:
                raise serializers.ValidationError({'choice_answer': 'This field is required.'})
            if kind == 'PARAGRAPH' and not text_answer:
                raise serializers.ValidationError({'text_answer': 'This field is required.'})

        if self.instance and editable is False:
            # If `self.instance` is not None, it means the instance
            # already exists, and is being updated
            raise serializers.ValidationError({'question': 'Answer cannot be updated for this question.'})
        return _data
