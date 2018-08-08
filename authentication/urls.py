from django.conf.urls import url
from .authentication import stlx_logout, stlx_register, delete, update_info, stlx_profile, activate_user
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path

urlpatterns = [
    url(r'^logout', stlx_logout, name='logout'),
    url(r'^register', stlx_register, name='register'),
    url(r'^profile', stlx_profile, name='profile'),
    url(r'^delete', delete, name='delete'),
    url(r'^update', update_info, name='updateinfo'),
    url(r'^obtain_token', obtain_jwt_token),
    url(r'^refresh_token', refresh_jwt_token),
    url(r'^verify_token', verify_jwt_token),
    path('activate_user/<str:token>', activate_user, name='activate_user')

]
