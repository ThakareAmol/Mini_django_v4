"""
## COMMAND
python manage.py shell
------------------------------------
from jobs.models import Portal
### TO INSERT NEW OBJECT IN DATABASE
Portal.objects.create(name="indeed.com", description="NEW")
-----------------------------------
# TO GET ALL THE OBJECTS
objs = Portal.objects.all()
for obj in objs:
    print(obj)
-----------------------------------
# TO FILTER PARTICULAR OBJECT BASED ON CERTAIN COLUMN
Portal.objects.get(name="naukri.com")
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Portal(models.Model):

    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def launch(self):
        self.save()


class JobTitle(models.Model):
    """
    jon title will have association of many portals
    `JobTitle` <--> `Portal` (one-to-many relationship)
    `JOb_description` <--> `Job-Title (one-to-one relationship)
    """
    title = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now)
    job_description = models.OneToOneField(
        "JobDescription", on_delete=models.CASCADE
    )
    portal = models.ForeignKey(Portal, on_delete=Portal)

    def __str__(self):
        return self.title + f"({self.portal})"


class JobDescription(models.Model):
    role = models.CharField(max_length=250)
    description_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role


class Applicant(models.Model):
    name = models.CharField(max_length=250, default="")
    applied_for = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=250)

    def __str__(self):
        return self.name



