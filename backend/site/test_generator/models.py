from django.db import models
from users.models import User
# Create your models here.

class Option(models.Model):
    def user_directory_path(instance, filename):
        return '{1}'.format(instance.user.id, filename)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    decision = models.FileField(blank=True, upload_to=user_directory_path)

class Task(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    task_number = models.IntegerField(max_length=5)
    example = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)