from django.contrib import admin

# Register your models here.
from .models import Steward, WorkStream, Stats

admin.site.register(WorkStream)
admin.site.register(Steward)
admin.site.register(Stats)
