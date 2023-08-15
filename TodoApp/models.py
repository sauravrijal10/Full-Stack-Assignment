from django.db import models
from user.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    completion = models.BooleanField(default=False)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completion']   