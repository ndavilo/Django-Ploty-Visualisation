from django import forms


class csvForm(forms.Form):
	myfile = forms.FileField()