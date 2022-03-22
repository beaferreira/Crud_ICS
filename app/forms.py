from django.forms import ModelForm
from app.models import Agente


class AgenteForm(ModelForm):
    class Meta:
        model = Agente
        fields = ['Nome', 'Classe', 'Função']
