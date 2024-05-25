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
    list_display = ('title', 'due_date', 'due_time', 'user', 'category', 'priority', 'completed', 'goal_image')
    list_filter = ('due_date', 'user', 'category', 'priority', 'completed')
    search_fields = ('title', 'additional_info')
    list_editable = ('completed',)
    list_display_links = ('title',)
    date_hierarchy = 'due_date'
    ordering = ('-due_date', 'priority')
    fieldsets = (
        (None, {
            'fields': ('title', 'due_date', 'due_time', 'additional_info', 'goal_image', 'goal_image_alt', 'category', 'new_category')
        }),
        ('Task Details', {
            'fields': ('user', 'category', 'priority', 'completed'),
        }),
    )

def get_readonly_fields(self, request, obj=None):
     # This method specifies which fields should be read-only in the admin interface.
    if obj: 
        return ['user']
    return []

def save_model(self, request, obj, form, change):

# This method overrides the default save behavior for the model in the admin interface.
    if not obj.user:
        obj.user = request.user
    obj.save()