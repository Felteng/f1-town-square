from django import forms
from .models import RaceEventComment


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