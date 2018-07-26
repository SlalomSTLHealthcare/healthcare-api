from api.models import Attendee
from django.views.generic.base import View
from utils import json_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect, HttpResponseBadRequest
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User



class Attendees(View):
    @staticmethod
    def get(request):
        '''Retrieve a list of all attendees.'''

        attendee_list = Attendee.objects.all().values()
        return json_response(attendee_list)

    @staticmethod
    def post(request):
        return json_response({})



         

