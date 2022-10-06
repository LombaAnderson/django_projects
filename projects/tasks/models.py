from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    # zip_code = models.IntegerField()
    # cost = models.IntegerField()
    # description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    # deadline = models.CharField(max_length= 150)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
