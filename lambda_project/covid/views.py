from django.core.serializers import serialize
from django.db.models import Count
from django.shortcuts import render

from covid.models import VsRaw

# Create your views here.


def covidListPageView(request):
    # template_name = 'covid_list.html'
    interaction_complexes = None
    farmacos = (
        VsRaw.objects.exclude(nm_farmaco="profluis")
        .values("id_pdb__nm_protein", "id_pdb", "nm_farmaco")
        .distinct("id_pdb__nm_protein")
    )
    if request == "POST":
        pass
    context = {
        "complexes": interaction_complexes,
        "farmacos": farmacos,
    }

    return render(request, "covid_list.html", context)
