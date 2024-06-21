from django.db import models

# Create your models here.
class sample(models.Model):
    name = models.CharField(max_length=100)
    sample_image = models.FileField(upload_to='images/sample')