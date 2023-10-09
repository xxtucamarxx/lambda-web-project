import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from vsview.models import PocketInteract
# Create your views here.

def interactionPageView(request):
    interaction = list(PocketInteract.objects.filter(id_pdb = '7KR1', id_pocket = 'pocket3').order_by('resnr'))
    serialized_interaction = serializers.serialize('json', interaction)
    output= json.dumps(json.loads(serialized_interaction), indent=4)
    return HttpResponse(output, content_type='application/json')

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

