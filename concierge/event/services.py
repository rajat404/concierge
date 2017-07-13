# Third Party Stuff
from django.utils import timezone

# Concierge Stuff
from concierge.base.utils import create_instance
from concierge.quiz.models import Quiz

from .models import OfflineEvent


def _create_quiz(slug, model_name):
    """Returns a `Quiz` object with the label
    of the specified foreign key and Event's Slug
    """
    label = '{}-{}'.format(slug, model_name)
    quiz_obj, _ = Quiz.objects.get_or_create(label=label)
    return quiz_obj


def create_event(serializer):
    """Creates a `Event` instance,
    and it's subsequent `OfflineEvent` instance
    """
    event_obj = create_instance(serializer)
    if event_obj.is_offline:
        OfflineEvent.objects.get_or_create(event=event_obj)

    # Sets foreign key relation to `Quiz` objects,
    # with the appropriate label,
    # for the newly created Event objects
    _slug = event_obj.slug
    event_obj.registration_quiz = _create_quiz(_slug, 'registration')
    event_obj.feedback_quiz = _create_quiz(_slug, 'feedback')

    _participation_open = event_obj.participation_open
    _participation_start = event_obj.participation_start
    _participation_end = event_obj.participation_end

    if _participation_open:
        # If `participation_start` is not given,
        # then it's set to current datetime
        if _participation_start in ('', None):
            event_obj.participation_start = timezone.now()
        # If `participation_end` is not given,
        # then it's set to Event's end datetime
        if _participation_end in ('', None):
            event_obj.participation_end = event_obj.end

    event_obj.save()
    return event_obj
