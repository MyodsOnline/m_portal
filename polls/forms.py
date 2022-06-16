from django import forms

from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
