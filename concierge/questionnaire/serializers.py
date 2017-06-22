from rest_framework import serializers

from concierge.base.serializers import DisplayChoiceField

from .models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    kind = DisplayChoiceField(choices=Questionnaire.RESPONSE_TYPES)

    class Meta:
        model = Questionnaire
        exclude = ('correct_choices',)

    def __init__(self, *args, **kwargs):
        super(QuestionnaireSerializer, self).__init__(*args, **kwargs)

        params = kwargs.get('data', None)
        if params:
            _kind = params.get('kind', None)
            _choices = params.get('choices', None)

            # If it's a MCQ, then `choices` shouldn't be empty
            if _kind == 'MCQ':
                self.fields['choices'] = serializers.JSONField(allow_null=False, required=True)

                # By default, `serializers.JSONField` accepts empty dicts
                # but if `choices` is mandatory, then `choices` shouldn't be an empty dict
                if _choices == {}:
                    raise serializers.ValidationError('For MCQs `choices` can`t be empty')
