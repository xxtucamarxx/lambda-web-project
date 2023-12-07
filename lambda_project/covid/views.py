from django.shortcuts import render
from covid.models import PlipSalt, PlipMetal, PlipWater, PlipHalogen, PlipHydrogen, PlipPication, PlipPistacking, PlipHydrophobic
from django.core.serializers import serialize

# update serializer
from django.utils.encoding import smart_str
from django.core.serializers.json import Serializer as Builtin_Serializer
from django.core.serializers import BUILTIN_SERIALIZERS

class Serializer(Builtin_Serializer):
    def get_dump_object(self, obj):
        self._current['id'] = smart_str(obj._get_pk_val(), strings_only=True)
        return self._current
BUILTIN_SERIALIZERS['json'] = Serializer

# Create your views here.

def covidListPageView(request):
    # template_name = 'covid_list.html'
    plip_interactions_query = None
    plip_interactions_list = [PlipSalt, PlipMetal, PlipWater, PlipHalogen, PlipHydrogen, PlipPication, PlipPistacking, PlipHydrophobic]
    id_pdb = None
    id_pocket = None
    if request.method == "POST":
        id_pdb = request.POST.get('pdb')
        id_pocket = request.POST.get('pocket')
        plip_interactions_query = {f'{x.__name__}': serialize(Serializer, x.objects.filter(id_pdb=id_pdb, id_pocket=f'pocket{id_pocket}')) for x in plip_interactions_list}
    context = {'plip_interactions': plip_interactions_query, 'id_pdb': id_pdb, 'id_pocket': id_pocket}

    return render(request, 'covid_list.html', context)
