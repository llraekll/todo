from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(null= True, blank=True)

    def __str__(self) -> str:
        return self.title