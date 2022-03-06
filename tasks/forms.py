from asyncio import Task
from dataclasses import fields
from re import M
from django.forms import ModelForm
from .models import Tasks


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title','desc','is_complete','tag']