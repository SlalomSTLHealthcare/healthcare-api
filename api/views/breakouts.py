from api.models import Breakout
from django.views.generic.base import View
from utils import json_response


class Breakouts(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all breakouts.'''

        breakout_list = Breakout.objects.all().values('title')
        return json_response(breakout_list)

    @staticmethod
    def post(request):
        return json_response({})
