from dataclasses import fields
from pyexpat import model
from django import forms


from .models import apply,Job

class ApplyForm(forms.ModelForm):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model= apply 
        fields=['name','email','website','cv','cover_letter']



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude=('slug','owner',)