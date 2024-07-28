from django import forms
from .models import QuillPost

class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'title',
            'description',
            'image',
            'content',
            'date',
        )