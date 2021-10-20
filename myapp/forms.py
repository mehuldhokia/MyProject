from django.forms import ModelForm, Textarea
from django import forms
from django.forms.widgets import TextInput, TextInput

from .models import Contact

class StudentForm(forms.Form):
    sname = forms.CharField(max_length=100)
    course = forms.CharField(max_length=50)
    sem = forms.IntegerField()


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'msg']
        labels = {
            'name'	:'Your Name',
            'email'	:'Email ID',
            'phone'	:'Contact No.',
            'msg'	:'Message',
        }
        widgets = {
            'name'  : TextInput(attrs={'placeholder':'Enter your name'}),
            'email' : TextInput(attrs={'type':'email'}),
            'phone' : TextInput(attrs={'type':'number'}),
            'msg'   : Textarea(attrs={'cols': 30, 'rows': 5}),
        }
