from django.db import models
from django.contrib.auth.models import AbstractUser

class Direction(models.Model):
  direction_name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50)

  def __str__(self):
    return str(self.direction_name)

class User(AbstractUser):
  birthday = models.DateField(blank=True, null=True)
  direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='user_direction', blank=True, null=True)
  phone_number = models.CharField(max_length=50, blank=True, null=True)
  img = models.ImageField(upload_to='user_images/', blank=True, null=True)
  telegram_link = models.CharField(max_length=200, blank=True, null=True)
  instagram_link = models.CharField(max_length=200, blank=True, null=True)
  facebook_link = models.CharField(max_length=200, blank=True, null=True)
  
  def __str__(self):
    return str(f'{self.first_name} {self.last_name}')