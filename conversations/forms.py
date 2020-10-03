from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Message
        fields = ['content']