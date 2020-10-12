from django.db import models
from django.urls import reverse

# Create your models here.
class Stand(models.Model):
  name = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  strings = models.IntegerField()
  make = models.CharField(max_length=100)
  cost = models.IntegerField()

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('detail', kwargs={'stand_id': self.id})