from django.db import models


# Create your models here.
class UploadFile(models.Model):
    file = models.ImageField(blank=False)
