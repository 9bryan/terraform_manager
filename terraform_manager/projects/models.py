from django.db import models

# Create your models here.
# MVC MODEL VIEW CONTROLLER

class Project(models.Model):
    title = models.CharField(max_length=120)
    git_url = models.CharField(max_length=120)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
