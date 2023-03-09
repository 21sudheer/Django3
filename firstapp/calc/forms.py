from calc.models import *
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

def validate(value):
        if "@gmail.com" in value:
             return value
        else:
             raise ValidationError("This field accepts mail id of google only")

class EmployeeForm(forms.ModelForm):
    Email=forms.EmailField(max_length=200, validators=[validate])
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        cleaned_data=super().clean()
        first_name=cleaned_data.get('first_name')
        last_name=cleaned_data.get('last_name')
        phone_number=cleaned_data.get('phone_number')
        Email=cleaned_data.get('Email')
        salary=cleaned_data.get('salary')
        
    
        
        if len(first_name) < 5:
            self._errors['first_name'] = self.error_class(['Minimum 5 characters required'])
            # raise ValidationError("fdfddfdfdf")
        if len(last_name) < 5:
            self._errors['last_name'] = self.error_class(['Minimum 5 characters required'])

        if str(phone_number)!= 10:
            self._errors['phone_number'] = self.error_class(['Minimum 10 digits required'])

        if float(salary) > 5:
            self._errors['salary'] = self.error_class(['Minimum 5 digits required'])

        return cleaned_data
        
    
 
        
    