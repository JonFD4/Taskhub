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
    list_display = ('title', 'due_date', 'due_time', 'user', 'category', 'priority', 'completed', 'goal_image')
    list_filter = ('due_date', 'user', 'category', 'priority', 'completed')
    search_fields = ('title', 'additional_info')
    list_editable = ('completed',)
    list_display_links = ('title',)
    date_hierarchy = 'due_date'
    ordering = ('-due_date', 'priority')
    fieldsets = (
        (None, {
            'fields': ('title', 'due_date', 'due_time', 'additional_info', 'goal_image', 'goal_image_alt')
        }),
        ('Task Details', {
            'fields': ('user', 'category', 'priority', 'completed'),
        }),
    )

   # This method specifies which fields should be read-only in the admin interface.
# When editing an existing object, the 'user' field is made read-only,
# ensuring it cannot be modified once set.
# When creating a new object, all fields remain editable.
def get_readonly_fields(self, request, obj=None):
    if obj: 
        return ['user']
    return []

# This method overrides the default save behavior for the model in the admin interface.
# It ensures that if the 'user' field is not set when saving the object,
# it is automatically assigned the current user.
def save_model(self, request, obj, form, change):
    if not obj.user:
        obj.user = request.user
    obj.save()





