from django import forms
from .models import Task
from django_summernote.widgets import SummernoteWidget

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'additional_info': SummernoteWidget(),
        }
