# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""
from rest_framework import routers

from concierge.concourse import api as concourse_api

router = routers.DefaultRouter(trailing_slash=False)

# Concourse
router.register(r'speakers', concourse_api.SpeakerViewset, base_name='speakers')
router.register(r'concourse', concourse_api.ConcourseViewset, base_name='concourse')
