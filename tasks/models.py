from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django_resized import ResizedImageField
from cloudinary_storage.storage import MediaCloudinaryStorage


class Category(models.Model):
    """
    Model representing a category for tasks.
    Categories help in organizing tasks into different groups.
    """
    name = models.CharField(max_length=100, help_text='Enter the category name (e.g., Work, Personal, etc.)')
    description = models.TextField(blank=True, null=True, help_text='Enter a description for the category')

    def __str__(self):
        return str(self.name)

class Task(models.Model):
    """
    Model representing a task.
    A task is an item that a user needs to track, complete, or manage.
    """
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
 
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, null=True, blank=True, help_text='The user who created the task')
    title = models.CharField(max_length=200, help_text='Enter the title of the task')
    due_date = models.DateField(help_text='Enter the due date for the task')
    due_time = models.TimeField(null=True, blank=True, help_text='Enter the due time for the task (optional)')
    additional_info = models.TextField(blank=True, null=True, help_text='Enter any additional information about the task')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, help_text='The category to which the task belongs')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, help_text='The priority level of the task')
    completed = models.BooleanField(default=False, help_text='Indicates if the task is completed')
    goal_image = ResizedImageField(size=[400, 300], quality=75, upload_to='goal_images/', storage=MediaCloudinaryStorage(), null=True, blank=True, help_text='Upload a resized image related to the goal (optional)')
    goal_image_alt = models.CharField(max_length=100, null=False, blank=True, help_text='Describe your image')

    def __str__(self):
        return str(self.title)
