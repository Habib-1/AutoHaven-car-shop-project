from .models import Comments
from django import forms 

class comment_form(forms.ModelForm):
    class Meta:
        model=Comments
        fields=[
            'name',
            'email',
            'comment_text',
        ]