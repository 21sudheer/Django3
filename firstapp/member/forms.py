from django import forms
class Employee(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=255)
    lastname = forms.CharField(label="Enter last name",max_length=255)
    phone = forms.IntegerField(max_length=10)
    Email = forms.EmailField(max_length=20)

