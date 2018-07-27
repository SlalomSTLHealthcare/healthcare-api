from django.conf.urls import url

from .views.people import People
from .views.sessions import Sessions
from .views.sponsors import Sponsors
from .views.schedules import Schedules
from .views.attendees import Attendees
from .views.sessions_attendees import Sessions_Attendees

urlpatterns = [
    url(r'^people$', People.as_view(), name='people'),
    url(r'^sessions$', Sessions.as_view(), name='sessions'),
    url(r'^sponsors$', Sponsors.as_view(), name='sponsors'),
    url(r'^schedules$', Schedules.as_view(), name='schedules'),
    url(r'^attendees$', Attendees.as_view(), name='attendees'),
    url(r'^session_attendees$', Sessions_Attendees.as_view(), name='session_attendees')

]
