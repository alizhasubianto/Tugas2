from django.forms import ModelForm
from todolist.models import Task

class Input_Form(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']