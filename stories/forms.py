from django import forms
from .models import Story, Comment


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'url')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.URLInput(attrs={'class':'form-control'}),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Comment body'}),
            }
