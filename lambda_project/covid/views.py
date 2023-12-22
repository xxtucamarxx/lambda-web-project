from django.shortcuts import render

from covid.models import VsRaw


# Create your views here.
def get_data_list(field: str, data):
    return data.values(field).distinct(field)


def covidListPageView(request):
    # template_name = 'covid_list.html'
    # data = VsRaw.objects.exclude(nm_farmaco="profluis", id_pdb="7K3G")
    #
    # proteins_list = get_data_list("id_pdb__nm_protein", data)
    # farmacos_list = get_data_list("nm_farmaco", data)

    context = {
        # "proteins_list": proteins_list,
        # "farmacos_list": farmacos_list,
    }

    if request.method == "POST":
        protein = request.POST.get("protein")
        context["protein"] = protein
        pdb = request.POST.get("pdb")
        farmaco = request.POST.get("farmaco")

        list_data = VsRaw.objects.exclude(nm_farmaco="profluis")
        if protein:
            list_data.filter(id_pdb__nm_protein=protein)
        if pdb:
            list_data.filter(id_pdb=pdb)
            context["pdb"] = pdb
        if farmaco:
            list_data.filter(nm_farmaco=farmaco)
            context["farmaco"] = farmaco

        context["complexes"] = list_data

    return render(request, "covid_list.html", context)
