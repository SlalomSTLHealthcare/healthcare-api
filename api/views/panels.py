from api.models import Panel
from django.views.generic.base import View
from utils import json_response


class Panels(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all panels.'''

        panel_list = Panel.objects.all().values()
        return json_response(panel_list)

    @staticmethod
    def post(request):
        return json_response({})
