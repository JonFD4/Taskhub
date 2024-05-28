from django import forms
from .models import Task, Category
from django_summernote.widgets import SummernoteWidget


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class TaskForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select category')

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'due_time', 'category', 'priority', 'completed', 'additional_info', 'goal_image', 'goal_image_alt']
        widgets = {
            'additional_info': SummernoteWidget(),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def save(self, commit=True):
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            self.instance.category = category
        return super().save(commit=commit)
