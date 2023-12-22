from django.urls import path

from covid.views import covidListPageView

urlpatterns = [
    path("covid/", covidListPageView, name="covid_list"),
]
