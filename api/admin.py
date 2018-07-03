from django.contrib import admin

from .models import Person
from .models import Session


admin.site.register(Person)
admin.site.register(Session)
