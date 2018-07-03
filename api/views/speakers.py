from api.models import Speaker
from django.views.generic.base import View
from utils import json_response


class Speakers(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all speakers.'''

        speaker_list = Speaker.objects.all().values('fullName')
        return json_response(speaker_list)

    @staticmethod
    def post(request):
        return json_response({})
