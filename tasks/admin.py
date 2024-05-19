from django.contrib import admin
from .models import Category, Task
from .forms import TaskForm 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ('title', 'due_date', 'due_time', 'user', 'category', 'priority', 'completed')
    list_filter = ('due_date', 'user', 'category', 'priority', 'completed')
    search_fields = ('title', 'additional_info')
    list_editable = ('completed',)
    list_display_links = ('title',)
    date_hierarchy = 'due_date'
    ordering = ('-due_date', 'priority')
    readonly_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': ('title', 'due_date', 'due_time', 'additional_info')
        }),
        ('Task Details', {
            'fields': ('user', 'category', 'priority', 'completed'),
        }),
    )
