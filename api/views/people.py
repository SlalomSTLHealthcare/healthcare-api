from api.models import Person
from django.views.generic.base import View
from utils import json_response


class People(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all speakers.'''

        person_list = Person.objects.all().values()
        return json_response(person_list)

    @staticmethod
    def post(request):
        return json_response({})
