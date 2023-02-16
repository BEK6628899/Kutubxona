from django import forms
from .models import *


class talaba_form(forms.Form):
    name = forms.CharField(min_length=3,max_length=30, label="Ism")
    course = forms.IntegerField(min_value=1,max_value=7, label="Kurs")
    books = forms.IntegerField(min_value=0, max_value=10, label="Kitob soni")
    gradute = forms.BooleanField(label="Bitiruvchi",required=False)


class muallif_form(forms.Form):
    name = forms.CharField(max_length=50,label="Ism")
    live = forms.ChoiceField(choices=[("ha","ha"),("yo`q","yo`q")],label="Trik")
    books = forms.IntegerField(label="Kitob soni")
    gender = forms.CharField(max_length=10,label="Jinsi")
    brithday = forms.DateField(label="Tug`ilgan sanasi")
    young = forms.IntegerField(label="Yoshi")


class kitob_form(forms.ModelForm):
    class Meta:
        model = kitob
        fields = ('__all__')  #("nom","sahifa")


class record_form(forms.ModelForm):
    class Meta:
        model = record
        fields = ("__all__")



class Admin_form(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ("__all__")
    # name = forms.CharField(max_length=50,label="Ism")
    # work_time = forms.DateField(label="Ish vaqti")





















