from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField
from concierge.base.utils import get_manager, get_object

from .models import Question, Quiz


class QuestionSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Question.ANSWER_TYPES)
    required = serializers.BooleanField(required=True)
    editable = serializers.BooleanField(required=True)
    quizzes = serializers.ListField(required=False, write_only=True, child=serializers.CharField())

    class Meta:
        model = Question
        fields = ('id', 'text', 'kind', 'required', 'editable', 'choices', 'quizzes',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        params = kwargs.get('data')
        if params:
            _kind = params.get('kind')
            # If it's a MCQ, then `choices` shouldn't be empty
            if _kind == 'MCQ':
                self.fields['choices'] = serializers.JSONField(allow_null=False, required=True)

    def validate_quizzes(self, quiz_label_list):
        quizzes = Quiz.objects.filter(label__in=quiz_label_list)
        if len(quiz_label_list) != len(quizzes):
            found_quizzes = list(quizzes.values_list('label', flat=True))
            error_text = "Invalid set of quiz labels. Only found {}".format(found_quizzes)
            raise serializers.ValidationError(error_text)
        return quizzes

    def validate_choices(self, choices):
        """Check that each choice contains all the choice attributes"""
        choice_attrs = {'value', 'type'}
        choice_types = list(dict(Question.CHOICE_TYPES).values())
        for choice in choices:
            option = choices[choice]
            if set(option.keys()) != choice_attrs:
                raise serializers.ValidationError('`value` & `type` are mandatory')
            type_value = option.get('type')
            if type_value not in set(choice_types):
                error_text = 'acceptable `type` values are : {}'.format(str(choice_types))
                raise serializers.ValidationError(error_text)
        return choices

    def validate(self, data):
        data = super().validate(data)
        kind = data.get('kind')
        choices = data.get('choices')

        if kind == 'MCQ':
            # By default, `serializers.JSONField` accepts empty dicts but if
            # `choices` is mandatory, then `choices` shouldn't be an empty dict
            if choices in ({}, None):
                raise serializers.ValidationError({'choices': 'This field is required for MCQs'})
        return data


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('id', 'label', 'questions',)


class QuizWriteSerializer(serializers.ModelSerializer):
    """`Quiz` instances shall only be created via `Concourse` creation.

    This Serializer deliberately removes the `unique=True` validation
    from `label` which the ModelSerializer imposes,
    in order to create a valid serializer instance,
    which will be used to validate & create `Question` objects
    """
    label = serializers.CharField(max_length=100)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ('id', 'label', 'questions',)

    def to_representation(self, obj):
        _label = obj.get('label')
        quiz_obj = get_object('quiz', 'Quiz', label=_label)
        return super().to_representation(quiz_obj)

    def validate_label(self, label):
        if get_manager('quiz', 'Quiz').filter(label=label).exists() is False:
            raise serializers.ValidationError('Quiz does not exist.')
        return label
