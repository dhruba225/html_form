from django.db import models

# Create your models here.
class School(models.Model):
    ScName=models.CharField(max_length=100,primary_key=True)
    ScHead=models.CharField(max_length=100)
    ScLoc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ScName

    