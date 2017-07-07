from django.utils import timezone

from concierge.base.utils import create_instance
from concierge.quiz.models import Quiz

from .models import OfflineConcourse


def _create_quiz(slug, model_name):
    """Returns a Quiz object with the label
    of the specified FK and Concourse's Slug
    """
    label = '{}-{}'.format(slug, model_name)
    quiz_obj, _ = Quiz.objects.get_or_create(label=label)
    return quiz_obj


def create_concourse(serializer):
    """Creates a `Concourse` instance,
    and it's subsequent `OfflineConcourse` instance
    """
    concourse_obj = create_instance(serializer)
    if concourse_obj.is_offline:
        OfflineConcourse.objects.get_or_create(concourse=concourse_obj)

    # Sets foreign key relation to Quiz objects,
    # with the appropriate label,
    # for the newly created Concourse objects
    _slug = concourse_obj.slug
    concourse_obj.registration_quiz = _create_quiz(_slug, 'registration')
    concourse_obj.feedback_quiz = _create_quiz(_slug, 'feedback')

    _participation_open = concourse_obj.participation_open
    _participation_start = concourse_obj.participation_start
    _participation_end = concourse_obj.participation_end

    if _participation_open:
        # If `participation_start` is not given,
        # then it's set to current datetime
        if _participation_start in ('', None):
            concourse_obj.participation_start = timezone.now()
        # If `participation_end` is not given,
        # then it's set to current datetime
        if _participation_end in ('', None):
            concourse_obj.participation_end = concourse_obj.end

    concourse_obj.save()
    return concourse_obj
