from django.conf.urls import url
from django.conf import settings
from the_eye_core.endpoint import EventProcessorAPI

urlpatterns = [
    url(r'^event-processor/$', EventProcessorAPI.as_view()),
]