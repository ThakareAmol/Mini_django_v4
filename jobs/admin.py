from django.contrib import admin

from jobs.models import Portal
from jobs.models import JobDescription, Applicant,JobTitle

# Register your models here.

admin.site.register(Portal)
admin.site.register(JobDescription)
admin.site.register(Applicant)
admin.site.register(JobTitle)