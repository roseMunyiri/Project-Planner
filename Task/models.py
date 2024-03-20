from django.db import models
from Project.models import AbstractBaseModel, Project
from Account.models import User

class Task(AbstractBaseModel):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('L', 'Low'),
        ('N', 'Normal'),
        ('U', 'Urgent'),
    ]
    STATUS_CHOICES = [
        ('I', 'Completed'),
        ('P', 'Pending'),
        ('IP', 'In Progress'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')