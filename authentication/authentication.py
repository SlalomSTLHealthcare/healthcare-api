from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
import json


def stlx_login(request):
    params = json.loads(request.body)
    email = params.get('email', '')
    password = params.get('password', '')

    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)

        return HttpResponse()
    else:
        return HttpResponseBadRequest(reason='Invalid username or password')


def stlx_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def stlx_register(request):
    params = json.loads(request.body)
    email = params.get('email', '')
    password = params.get('password', '')
    if User.objects.filter(email=email).exists():
        return HttpResponseBadRequest(reason='A user exists for this email address.')

    if User.objects.filter(username=email).exists():
        return HttpResponseBadRequest(reason='Sorry, this username is taken.')

    try:
        User.objects.create_user(username=email,password=password,email=email)
        user = authenticate(username=email, password=password)
    except Exception as e:
        print(str(e))
        return HttpResponseServerError(reason=str(e))

    try:
        user.is_active = False
        user.save()
        login(request, user)
        return HttpResponse()
    except Exception as e:
        print(str(e))
        return HttpResponseServerError(reason=str(e))
