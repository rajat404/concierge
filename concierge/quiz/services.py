# Concierge Stuff
from concierge.base.utils import create_instance, get_object

from .serializers import QuestionSerializer


def create_question(serializer):
    question_obj = create_instance(serializer)
    # `quizzes` is the `Quiz` queryset which we obtain
    # while validating the `quizzes` field
    quizzes = serializer.validated_data.get('quizzes')
    if quizzes:
        for quiz_obj in quizzes:
            quiz_obj.questions.add(question_obj)
    return question_obj


def create_quiz(serializer):
    serializer.is_valid(raise_exception=True)
    _label = serializer.validated_data.get('label')
    _questions = serializer.validated_data.get('questions')
    quiz_obj = get_object('quiz', 'Quiz', label=_label)
    for question in _questions:
        question_serializer = QuestionSerializer(data=question)
        question_obj = create_instance(serializer=question_serializer)
        if question_obj:
            quiz_obj.questions.add(question_obj)
    return quiz_obj
