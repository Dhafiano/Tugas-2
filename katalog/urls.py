# TODO: Implement Routings Here
from django.urls import path
from katalog.views import showkatalog

app_name = "katalog"

urlpatterns = [
    path('', showkatalog, name='katalog'),
]