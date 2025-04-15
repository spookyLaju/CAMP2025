from . models import Youth
from django import forms 


class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control '}),
            "email": forms.EmailInput(attrs={'class': 'form-control '}),
            "phone": forms.TextInput(attrs={'class': 'form-control '}),
            "date_of_birth": forms.DateInput(attrs={'class': 'form-control '}),
            "branch": forms.TextInput(attrs={'class': 'form-control '}),
            "district": forms.TextInput(attrs={'class': 'form-control '}),
            "department": forms.TextInput(attrs={'class': 'form-control '}),
        }