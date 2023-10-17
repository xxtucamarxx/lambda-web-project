from django import forms

# from vsview.models import PocketInteract
# class InteractionQueryForm(forms.ModelForm):
#     class Meta:
#         model = PocketInteract
#         fields = ['id_pdb', 'id_pocket']

class PlipListForm(forms.Form):
    id_pdb = forms.CharField(label="Proteina", max_length=4)
    id_pocket = forms.CharField(label="Pocket", max_length=20)
