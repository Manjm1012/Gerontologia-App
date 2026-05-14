from django import forms

from .models import Medicamentos


class MedicamentoManualForm(forms.ModelForm):
    observaciones = forms.CharField(required=False)
    empleado_encargado = forms.CharField(required=False)

    class Meta:
        model = Medicamentos
        fields = ["paciente", "nombre_medicamento", "dosis", "observaciones", "empleado_encargado"]
