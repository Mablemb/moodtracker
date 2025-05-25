from django import forms
from .models import RegistroHumor, HumorEscolha

class RegistroHumorForm(forms.ModelForm):
    # Você pode customizar o widget do campo de humor aqui se quiser,
    # por exemplo, para usar radio buttons em vez de um select.
    # humor = forms.ChoiceField(choices=HumorEscolha.choices, widget=forms.RadioSelect)

    class Meta:
        model = RegistroHumor
        # Quais campos do modelo RegistroHumor devem aparecer no formulário?
        # O 'usuario' será preenchido automaticamente na view com o usuário logado.
        # A 'data_registro' é auto_now_add.
        fields = ['humor', 'sentimento_principal', 'notas_adicionais']

        widgets = {
            'humor': forms.Select(attrs={'class': 'form-control'}),
            'sentimento_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Como você está se sentindo mais especificamente?'}),
            'notas_adicionais': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Algum detalhe adicional?'}),
        }

        labels = {
            'humor': 'Como você está se sentindo hoje?',
            'sentimento_principal': 'Sentimento principal',
            'notas_adicionais': 'Notas adicionais',
        }