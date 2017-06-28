# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""
from rest_framework import routers

from concierge.concourse import api as concourse_api
from concierge.participant import api as participant_api
from concierge.quiz import api as quiz_api
from concierge.registration import api as registration_api

router = routers.DefaultRouter(trailing_slash=False)

# Concourse
router.register(r'speaker', concourse_api.SpeakerViewset, base_name='speaker')
router.register(r'concourse', concourse_api.ConcourseViewset, base_name='concourse')

# Participant
router.register(r'participant', participant_api.ParticipantViewset, base_name='participant')

# Quiz
router.register(r'question', quiz_api.QuestionViewset, base_name='question')
router.register(r'quiz', quiz_api.QuizViewset, base_name='quiz')

# Registration
router.register(r'registration', registration_api.RegistrationAnswerViewset, base_name='registration')
router.register(r'registrationquiz', registration_api.RegistrationQuizViewset, base_name='registrationquiz')

# Feedback
# router.register(r'feedback', feedback_api.FeedbackViewset, base_name='feedback')
