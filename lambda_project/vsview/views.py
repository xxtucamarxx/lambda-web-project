import json
from django.views.generic import TemplateView
from vsview.forms import PlipQueryForm
from vsview.models import PocketInteract
from django.shortcuts import render
# Create your views here.
#

def plipListPageView(request):
    interactions = None
    id_pdb = None
    id_pocket = None
    if request.method == "POST":
        form = PlipQueryForm(request.POST)
        if form.is_valid():
            id_pdb = form.cleaned_data['id_pdb']
            id_pocket = form.cleaned_data['id_pocket']
            interactions = PocketInteract.objects.filter(id_pdb=id_pdb, id_pocket=id_pocket)
    else:
        form = PlipQueryForm()
    context = {'form': form, 'interactions': interactions, 'id_pdb': id_pdb, 'id_pocket': id_pocket}

    return render(request, 'plip_list.html', context)
    # template_name = 'interaction_query.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

