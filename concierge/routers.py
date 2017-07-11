# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""
from rest_framework import routers

from concierge.answer import api as answer_api
from concierge.event import api as event_api
from concierge.participant import api as participant_api
from concierge.quiz import api as quiz_api

router = routers.DefaultRouter(trailing_slash=False)

# Event
router.register(r'speaker', event_api.SpeakerViewset, base_name='speaker')
router.register(r'event', event_api.EventViewset, base_name='event')

# Participant
router.register(r'participant', participant_api.ParticipantViewset, base_name='participant')

# Quiz
router.register(r'question', quiz_api.QuestionViewset, base_name='question')
router.register(r'quiz', quiz_api.QuizViewset, base_name='quiz')
router.register(r'quizupload', quiz_api.QuizUploadViewset, base_name='quizupload')

# Answer
router.register(r'answer', answer_api.AnswerViewset, base_name='answer')
