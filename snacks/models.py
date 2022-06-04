from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
  # create Snack model

  # add name as CharField with max len of 64 char
  name = models.CharField(max_length=256)

  # add purchaser as ForeignKey related to built in user model w/ CASCADE del opt
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  
  # add description TextField
  description = models.TextField(max_length=500)
  
  # user friendly display in admin
  def __str__(self):
        return self.name