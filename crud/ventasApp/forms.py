from django import forms

class departamentoForm(forms.Form):
    actualizar_localidad = forms.CharField(widget=forms.TextInput,help_text="Ingrese la nueva Localidad")
    #(max_length=10,blank=False,help_text="Ingrese la nueva Localidad")