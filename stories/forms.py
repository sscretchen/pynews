from django import forms
from .models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'url')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.URLInput(attrs={'class':'form-control'}),
            }
