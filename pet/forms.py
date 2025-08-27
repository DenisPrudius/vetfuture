from pet.models import Operation, Pet
from django import forms


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["doctors", "pet", "description"]
        widgets = {
            "doctors": forms.CheckboxSelectMultiple(),
            "description": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "pet": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "doctors": "Доктори",
            "pet": "Тваринка",
            "description": "Опис операціїї"
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["nickname", "age"]
        labels = {
            "nickname": "Кличка",
            "age": "Вік",
        }
        widgets = {
            "nickname": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введіть ім’я"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
        }