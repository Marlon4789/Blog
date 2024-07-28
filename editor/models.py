from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField

class QuillPost(models.Model):
    title = models.CharField(null=True, max_length=200, blank=False, unique=True)
    description = models.CharField(null=True, max_length=200, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = QuillField()
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title
