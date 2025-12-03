from django.db import models

# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        INPROGRES = "INPROGRES", "In Progres"
        COMPLETED = "COMPLETED", "Completed"

    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)