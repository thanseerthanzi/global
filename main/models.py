from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)