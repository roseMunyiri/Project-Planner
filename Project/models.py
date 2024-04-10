from django.db import models
from Account.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('O', 'Ongoing'),
        ('C', 'Completed'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    attachments = models.FileField(upload_to='projects/', default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    @property
    def project_duration(self):
        if self.start_date and self.due_date:
            project_duration = self.start_date - self.due_date
            return project_duration 
        else:
            return None
        
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('L', 'Low'),
        ('N', 'Normal'),
        ('U', 'Urgent'),
    ]
    STATUS_CHOICES = [
        ('C', 'Completed'),
        ('P', 'Pending'),
        ('IP', 'In Progress'),
    ]
    
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    attachments = models.FileField(upload_to='tasks/', default='')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task')
    