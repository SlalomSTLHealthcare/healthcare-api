from api.models import Session_Attendee
from django.views.generic.base import View
from utils import json_response


class Sessions_Attendees(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all panels.'''

        session_attendee_list = Session_Attendee.objects.all().values()
        return json_response(session_attendee_list)

    @staticmethod
    def post(request):
        return json_response({})
