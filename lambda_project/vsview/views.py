from django.views.generic import TemplateView
from vsview.forms import PlipListForm
from vsview.models import PocketInteract
from django.shortcuts import render
# Create your views here.
#

def plipListPageView(request):
    if request.method == "POST":
        form = PlipListForm(request.POST)
        if form.is_valid():
            id_pdb = form.cleaned_data['id_pdb']
            id_pocket = form.cleaned_data['id_pocket']
            interactions = PocketInteract.objects.filter(id_pdb=id_pdb, id_pocket=id_pocket)
        else:
            interactions = None
    else:
        form = PlipListForm()
        interactions = None
    context = {'form': form, 'interactions': interactions}

    return render(request, 'plip_list.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

