from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    salary=models.IntegerField(max_length=100)

    def __str__(self):
        return self.name

