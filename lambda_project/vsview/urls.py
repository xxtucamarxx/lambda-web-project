
from django.urls import path
from vsview.views import AboutPageView, HomePageView, interactionPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('interaction/', interactionPageView, name='interaction'),
    path('about/', AboutPageView.as_view(), name='about')
]
