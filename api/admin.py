from django.contrib import admin

from .models import Person
from .models import Session
from .models import Schedule
from .models import Sponsor


admin.site.register(Person)
admin.site.register(Session)
admin.site.register(Schedule)
admin.site.register(Sponsor)
