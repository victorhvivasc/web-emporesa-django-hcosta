from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={"class":"form-control" }))
    mail= forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs={"class":"form-control"}))
    content= forms.CharField(label='Contenido', required=True, widget= forms.Textarea(attrs={"class":"form-control", 
                                                                                        "rows":3, 
                                                                                        "placeholder":"Escribe tu mensaje"}),
                                                                                        min_length=50, max_length=500)
