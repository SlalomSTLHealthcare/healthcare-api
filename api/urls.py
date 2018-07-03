from django.conf.urls import url

from .views.people import People
from .views.sessions import Sessions

urlpatterns = [
    url(r'^people$', People.as_view(), name='people'),
    url(r'^sessions$', Sessions.as_view(), name='sessions')
]
