from django.db import models

class Text(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.id
