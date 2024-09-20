from django.db import models

class Members (models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.age}"


# Create your models here.
