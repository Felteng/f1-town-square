from django import forms
from .models import RaceEventComment


# Form class from: https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/blog/forms.py
class RaceCommentForm(forms.ModelForm):
    class Meta:
        model = RaceEventComment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your thoughts',
            }),
        }
