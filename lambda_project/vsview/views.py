from django.views.generic import TemplateView
<<<<<<< HEAD
from vsview.forms import PlipListForm
=======
>>>>>>> tuca
from vsview.models import PocketInteract
from django.shortcuts import render
# Create your views here.

def plipListPageView(request):
<<<<<<< HEAD
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
=======
    # template_name = 'plip_list.html'
    interactions = None
    id_pdb = None
    id_pocket = None
    if request.method == "POST":
        id_pdb = request.POST.get('pdb')
        id_pocket = request.POST.get('pocket')
        interactions = PocketInteract.objects.filter(id_pdb=id_pdb, id_pocket=f'pocket{id_pocket}')
    context = {'interactions': interactions, 'id_pdb': id_pdb, 'id_pocket': id_pocket}
>>>>>>> tuca

    return render(request, 'plip_list.html', context)


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

