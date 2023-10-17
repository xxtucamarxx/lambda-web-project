
from django.urls import path
from vsview.views import AboutPageView, HomePageView, interactionQueryPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('plip', interactionQueryPageView, name='plip_list'),
    path('about/', AboutPageView.as_view(), name='about')
]
