from django.conf.urls import url
from .authentication import stlx_logout, stlx_register, delete, update_info, stlx_profile, decode_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^logout', stlx_logout, name='logout'),
    url(r'^register', stlx_register, name='register'),
    url(r'^profile', stlx_profile, name='profile'),
    url(r'^delete', delete, name='delete'),
    url(r'^update', update_info, name='updateinfo'),
    url(r'^obtain_token', obtain_jwt_token),
    url(r'^refresh_token', refresh_jwt_token),
    url(r'^verify_token', verify_jwt_token),
]
