from django import forms
from .templates.tasks import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ('name', 'project', 'description', 'deadline', 'is_done', )
