from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Email", required=True)
    mensaje=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)