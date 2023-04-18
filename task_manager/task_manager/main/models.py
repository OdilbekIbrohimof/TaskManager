from django.db import models
from account.models import User, Direction

class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, blank=True, related_name='group_members')
    added_date = models.DateField(auto_now_add=True)
    direction = models.ForeignKey(Direction, on_delete=models.PROTECT)
    moderator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)

class Task(models.Model):
    name = models.CharField(max_length=250)
    link = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='task_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return str(self.name)