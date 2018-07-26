from django.contrib.auth.models import User
from api.models import Attendee
from api.models import Session_Attendee
from api.models import Session
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from utils import json_response
from django.forms.models import model_to_dict



@csrf_exempt
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
def stlx_profile(request):
    params = json.loads(request.body)
    email = params.get('email', '')
    user = User.objects.get(email=email)
    session_attendee_list = list(Session_Attendee.objects.filter(attendee_id=user.attendee.id).values())
    user_fields = {'first_name', 'last_name', 'email'}
    attendee_fields = {'company', 'position', 'twitter', 'lunch', 'diet', 'diet_allergy', 'tshirt_size', 'comment', 'donate'}
    result={
        "user": model_to_dict(instance=user,fields=user_fields),
        "attendee": model_to_dict(instance=user.attendee,fields=attendee_fields),
        "sessions": session_attendee_list
    }
    try:
        return json_response(result)
    except User.DoesNotExist:
        return None

@csrf_exempt
def stlx_register(request):
    params = json.loads(request.body)
    email = params.get('email', '')
    password = params.get('password', '')
    first_name = params.get('firstName', '')
    last_name = params.get('lastName', '')

    if User.objects.filter(email=email).exists():
        return HttpResponseBadRequest(reason='A user exists for this email address.')

    if User.objects.filter(username=email).exists():
        return HttpResponseBadRequest(reason='Sorry, this username is taken.')

    try:
        User.objects.create_user(username=email,password=password,email=email, first_name=first_name, last_name=last_name)
        user = authenticate(username=email, password=password)
    except Exception as e:
        print(str(e))
        return HttpResponseServerError(reason=str(e))

    try:
        user.is_active = False
        update_attendee(params, email)
        login(request, user)
        return HttpResponse()
    except Exception as e:
        print(str(e))
        return HttpResponseServerError(reason=str(e))

def update_attendee(params, user_email):
    user_id = User.objects.get(email = user_email).id
    user = User.objects.get(pk = user_id)
    user.attendee.comment = params.get('comment', '')
    user.attendee.firstName = params.get('firstName', '')
    user.attendee.lastName = params.get('lastName', '')
    user.attendee.company = params.get ('company', '')
    user.attendee.position = params.get('position', '')
    user.attendee.twitter = params.get('twitter', '')
    user.attendee.lunch = params.get('lunch', True)
    user.attendee.diet = params.get('diet', [])
    user.attendee.diet_allergy = params.get('allergies', '')
    user.attendee.tshirt_size = params.get('size', '')
    user.attendee.donate = params.get('donate', True)
    breakout_one = Session.objects.get(pk = params.get('breakout_one'))
    max_capacity_one = Session.objects.get(pk = params.get('breakout_one')).max_capacity
    breakout_two = Session.objects.get(pk = params.get('breakout_two'))
    max_capacity_two = Session.objects.get(pk = params.get('breakout_two')).max_capacity
    Session_Attendee.objects.create(attendee=user.attendee, session=breakout_one, date_signedup=datetime.datetime.now(), session_max_capacity=max_capacity_one, session_tag=1)
    Session_Attendee.objects.create(attendee=user.attendee, session=breakout_two, date_signedup=datetime.datetime.now(), session_max_capacity=max_capacity_two, session_tag=2)
    breakout_one_waitlist_id = params.get('breakout_oneWait')
    breakout_two_waitlist_id = params.get('breakout_twoWait')

    if breakout_one_waitlist_id  != '':
        breakout_oneWait = Session.objects.get(pk = breakout_one_waitlist_id)
        max_capacity_oneWait = Session.objects.get(pk = breakout_one_waitlist_id).max_capacity
        Session_Attendee.objects.create(attendee=user.attendee, session=breakout_oneWait, date_signedup=datetime.datetime.now(), session_max_capacity=max_capacity_oneWait, session_tag=1 )

    if breakout_two_waitlist_id != '':
        breakout_twoWait = Session.objects.get(pk = breakout_two_waitlist_id)
        max_capacity_twoWait = Session.objects.get(pk = breakout_two_waitlist_id).max_capacity
        Session_Attendee.objects.create(attendee=user.attendee, session=breakout_twoWait, date_signedup=datetime.datetime.now(), session_max_capacity=max_capacity_twoWait, session_tag=2)

    user.save()


@csrf_exempt
def delete(request):
    params = json.loads(request.body)
    email = params.get('email', '')
    user = User.objects.get(email=email)

    if User.objects.filter(email=email).exists():
        try:
           user.delete()
        except Exception as e:
            print(str(e))
            return HttpResponseServerError(reason=str(e))
    else:
        return HttpResponseBadRequest(reason='Attendee does not exist')

    return HttpResponse()

@csrf_exempt
def update_info(request):
    params = json.loads(request.body)
    updated_email = params.get('updatedEmail','')
    user_email = params.get('email', '')
    user = User.objects.get(email=user_email)


    if User.objects.filter(email=updated_email).exists():
        return HttpResponseBadRequest(reason='Email already in use')
    else:
        import pdb; pdb.set_trace()
        # try:
        #     #if Session_Attendee.objects.filter(attendee_id=user.attendee.id).exists():
        # except Exception as e:
        #     print(str(e))
        #     return HttpResponseServerError(reason=str(e))
        update_attendee(params, user_email)
        user.email = params.get('updatedEmail', '')
        user.username = params.get('updatedEmail', '')
        user.firstName = params.get('firstName', '')
        user.lastName = params.get('lastName', '')
        user.save()

    return HttpResponse()
