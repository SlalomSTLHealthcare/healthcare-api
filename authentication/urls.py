from django.conf.urls import url
from .authentication import stlx_login, stlx_logout, stlx_register, delete

urlpatterns = [
    url(r'^login', stlx_login, name='login'),
    url(r'^logout', stlx_logout, name='logout'),
    url(r'^register', stlx_register, name='register'),
    url(r'^delete', delete, name='delete')
]
