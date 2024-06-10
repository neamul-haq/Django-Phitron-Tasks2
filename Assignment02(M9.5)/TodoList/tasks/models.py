from django.db import models
# Create your models here.
class Tasks(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.taskTitle