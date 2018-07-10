from api.models import Schedule
from django.views.generic.base import View
from utils import json_response


class Schedules(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all schedules.'''

        schedule_list = Schedule.objects.all().values()
        return json_response(schedule_list)

    @staticmethod
    def post(request):
        return json_response({})
