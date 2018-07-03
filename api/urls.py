from django.conf.urls import url

from .views.speakers import Speakers
from .views.panels import Panels
from .views.breakouts import Breakouts

urlpatterns = [
    url(r'^speakers$', Speakers.as_view(), name='speakers'),
    url(r'^panels$', Panels.as_view(), name='panels'),
    url(r'^breakouts$', Breakouts.as_view(), name='breakouts')
]
