
from django.urls import path
from vsview.views import AboutPageView, HomePageView, interactionQueryPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('interaction/query', interactionQueryPageView, name='interaction_query'),
    path('about/', AboutPageView.as_view(), name='about')
]
