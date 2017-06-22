# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""
from rest_framework import routers

from concierge.concourse import api as concourse_api
from concierge.participant import api as participant_api
from concierge.questionnaire import api as questionnaire_api
from concierge.registration import api as registration_api
from concierge.feedback import api as feedback_api

router = routers.DefaultRouter(trailing_slash=False)

# Concourse
router.register(r'speaker', concourse_api.SpeakerViewset, base_name='speaker')
router.register(r'concourse', concourse_api.ConcourseViewset, base_name='concourse')

# Participant
router.register(r'participant', participant_api.ParticipantViewset, base_name='participant')

# Questionnaire
router.register(r'questionnaire', questionnaire_api.QuestionnaireViewset, base_name='questionnaire')

# Registration
router.register(r'registration', registration_api.RegistrationViewset, base_name='registration')

# Feedback
router.register(r'feedback', feedback_api.FeedbackViewset, base_name='feedback')
