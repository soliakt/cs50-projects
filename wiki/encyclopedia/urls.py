from django.urls import path

from . import views

# This app_name is not acc needed bc we only have 1 app,
# but it's worth having in case we have multiple apps.
# What it makes is, in case we add a link, it lets Django 
# find out what app you're refering to when linking.
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("404", views.error_404, name="404"),
    path("entries/<str:entry_title>", views.content_page, name="contentPage")
]
