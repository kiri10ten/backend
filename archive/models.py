from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters


class Subject(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title',)


class Archive(models.Model):
    subject = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='subject', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
        return defaultfilters.date(self.created_at, 'M d, Y')