from django.contrib import admin

from .models import Person
from .models import Session
from .models import Schedule
from .models import Sponsor
from .models import Attendee
from .models import EmailSignUp
from .models import SponsorQuery


admin.site.register(Person)
admin.site.register(Session)
admin.site.register(Schedule)
admin.site.register(Sponsor)
admin.site.register(Attendee)
admin.site.register(EmailSignUp)
admin.site.register(SponsorQuery)
