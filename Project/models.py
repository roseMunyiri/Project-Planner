from django.db import models
from Account.models import User

class AbstractBaseModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    attachments = models.FileField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class meta:
        abstract= True

class Project(AbstractBaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='projects', null=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_projects', null=True, blank=True)