from api.models import sponsor
from django.views.generic.base import View
from utils import json_response


class Sponsors(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all Sponsors.'''

        sponsor_list = Sponsor.objects.all().values()
        return json_response(sponsor_list)

    @staticmethod
    def post(request):
        return json_response({})
