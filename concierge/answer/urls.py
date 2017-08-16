from django.conf.urls import url
from .views import answer_test

urlpatterns = [
    url(r'^answer/$', answer_test, name='answer_test'),
]
