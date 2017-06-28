from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Question, Quiz


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Question.ANSWER_TYPES)
    required = serializers.BooleanField(required=True)
    editable = serializers.BooleanField(required=True)

    class Meta:
        model = Question
        exclude = ('correct_choices',)

    def __init__(self, *args, **kwargs):
        super(QuestionSerializer, self).__init__(*args, **kwargs)
        params = kwargs.get('data', None)
        if params:
            _kind = params.get('kind', None)
            # If it's a MCQ, then `choices` shouldn't be empty
            if _kind == 'MCQ':
                # self.fields['choices'] = MCQChoicesField(allow_null=False, required=True)
                self.fields['choices'] = serializers.JSONField(allow_null=False, required=True)

    def validate(self, data):
        super(QuestionSerializer, self).validate(data)
        kind = data.get('kind')
        choices = data.get('choices')
        if kind == 'MCQ':
            # By default, `serializers.JSONField` accepts empty dicts
            # but if `choices` is mandatory, then `choices` shouldn't be an empty dict
            if choices in ({}, None):
                raise serializers.ValidationError({'choices': 'This field is required for MCQs'})

            # Check that each choice contains all the choice attributes
            choice_attrs = {'value', 'type'}
            choice_types = list(dict(Question.CHOICE_TYPES).values())
            for choice in choices:
                option = choices[choice]
                if set(option.keys()) != choice_attrs:
                    error_key = '{} => {} => {}'.format('choices', str(choice), str(option))
                    error_text = '`value` & `type` are mandatory'
                    raise serializers.ValidationError({error_key: error_text})
                type_value = option.get('type')
                if type_value not in set(choice_types):
                    error_key = '{} => {} => {}'.format('choices', str(choice), str(option))
                    error_text = 'acceptable `type` values are : {}'.format(str(choice_types))
                    raise serializers.ValidationError({error_key: error_text})
        return data
