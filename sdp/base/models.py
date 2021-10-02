from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    mobile_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
