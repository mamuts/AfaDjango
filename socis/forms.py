from django import forms
from .models import Importar

class ImportarForm(forms.ModelForm):

    class Meta:
        model = Importar
        fields = ["importar_ruta"]
        widget = {
            "name": forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
