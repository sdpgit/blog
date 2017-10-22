from django import forms

from .models import BlogPost


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': 'text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
