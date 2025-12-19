# apps/files/models.py
from django.db import models

class File(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads/')
    code = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.code} → {self.filename}"
