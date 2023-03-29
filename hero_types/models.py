from django.db import models

# Create your models here.
class Super_types(models.Model):
    type = models.CharField(max_length=255)



class Types_h_v(models.Model):
    side = models.CharField(max_length=255)

    