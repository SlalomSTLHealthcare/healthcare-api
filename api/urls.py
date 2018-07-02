from django.conf.urls import url

from .views.speakers import Speakers

urlpatterns = [
    url(r'^speakers$', Speakers.as_view(), name='speakers')
]
