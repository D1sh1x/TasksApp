from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Введите название",
                "class": "form-control"
            }),
            "task": Textarea(attrs={
                "placeholder": "Введите описание",
                "class": "form-control"
            }),
        }