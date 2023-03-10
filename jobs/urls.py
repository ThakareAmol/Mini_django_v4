from django.urls import path, re_path
from . import views  # import from current directory
from .views import get_portal_details, get_job_description

urlpatterns = [
    re_path(r"^wel*", views.welcome, name="welcome"),
    path("portal/", views.get_portal_details, name="details"),
    path("jobtitles/", views.job_titles, name="jobtitles"),
    path("<int:job_id>/", views.get_job_description, name="JD"),

]

##########################################################
# How to capture PATH parameters from URL?               #
##########################################################
# Notes:
#
# To capture a value from the URL, use angle brackets.
# Captured values can optionally include a converter type.
# For example, use <int:name> to capture an integer parameter.
# If a converter isn’t included,
# any string, excluding a / character, is matched.
# There’s no need to add a leading slash, because every URL has that.
# For example, it’s articles, not /articles.

##########################################################