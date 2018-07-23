from api.models import Session
from django.views.generic.base import View
from utils import json_response


class Sessions(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all panels.'''

        session_list = Session.objects.all().values()
        return json_response(session_list)

    @staticmethod
    def post(request):
        return json_response({})
