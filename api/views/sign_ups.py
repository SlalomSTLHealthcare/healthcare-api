from api.models import EmailSignUp
from api.models import SponsorQuery
from django.views.generic.base import View
from django.http import HttpResponseBadRequest
from utils import json_response
import json


class EmailSignUpView(View):
    @staticmethod
    def post(request):
        params = json.loads(request.body)
        email = params.get('email', '')

        try:
            esu = EmailSignUp(email=email)
            esu.save()
        except Exception as e:
            print(str(e))
            return HttpResponseBadRequest(reason=str(e))

        return json_response({'status': 'success'})


class SponsorQueryView(View):
    @staticmethod
    def post(request):
        params = json.loads(request.body)
        email = params.get('email', '')
        company = params.get('company', None)
        notes = params.get('notes', None)
        notes = params.get('name', None)

        try:
            sq = SponsorQuery(email=email, company=company, notes=notes, name=name)
            sq.save()
        except Exception as e:
            print(str(e))
            return HttpResponseBadRequest(reason=str(e))

        return json_response({'status': 'success'})
