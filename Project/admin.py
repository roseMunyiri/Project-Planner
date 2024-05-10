from django.contrib import admin
from .models import Project, Task
from Account.models import User

admin.site.register(Project)
admin.site.register(Task)


