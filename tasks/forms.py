from django import forms
from .models import Task
from django_summernote.widgets import SummernoteWidget

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'due_time', 'category', 'priority', 'completed', 'additional_info', 'goal_image', 'goal_image_alt']
        widgets = {
            'additional_info': SummernoteWidget(),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
        }
