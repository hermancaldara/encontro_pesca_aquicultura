from django import forms
from models import Inscricao


class InscricaoForm(forms.ModelForm):

    class Meta:
    
        model = Inscricao
        widgets ={
            'apresenta_trabalho' : forms.RadioSelect, 
        }
