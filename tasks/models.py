from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django_resized import ResizedImageField
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.contrib.auth import get_user_model


class Category(models.Model):
    """
    Model representing a category for tasks.
    Categories help in organizing tasks into different groups.
    """
    name = models.CharField(max_length=100, help_text='Enter the category name (e.g., Work, Personal, etc.)')
    description = models.TextField(blank=True, null=True, help_text='Enter a description for the category')
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)

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
 
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    due_time = models.TimeField(null=True, blank=True, help_text='Enter the due time for the task (optional)')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False,)
    additional_info = models.TextField(blank=True, null=True, help_text='Enter any additional information about the task')
    goal_image = ResizedImageField(size=[400, 300], quality=75, upload_to='goal_images/', storage=MediaCloudinaryStorage(), null=True, blank=True, help_text='Upload an image related to the goal (optional)')
    goal_image_alt = models.CharField(max_length=100, null=False, blank=True, help_text='Describe your image')

    def __str__(self):
        return str(self.title)
