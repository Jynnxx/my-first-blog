from django.db import models
from django.utils import timezone

class Image(models.Model):
    name = models.CharField(max_length = 50)
    file = models.FileField(upload_to = 'media/')
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name