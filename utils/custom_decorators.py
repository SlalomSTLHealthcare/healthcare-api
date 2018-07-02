from functools import wraps
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.utils.decorators import method_decorator


def login_required(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return func(request, *args, **kwargs)
    return inner


class LoginView(View):
    @method_decorator(login_required)
    # dispatch looks at the request to determine whether it is a GET,
    # POST, etc, and relays the request to a matching method if one
    # is defined, or raises HttpResponseNotAllowed if not:
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)
