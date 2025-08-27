from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin

from pet_health_info.models import PetHealthInfo


class PetHealthInfoCreateForm(UserPassesTestMixin, forms.ModelForm):
    class Meta:
        model = PetHealthInfo
        fields = ["pet", "diagnosis", "recommendation"]
        labels = {
            "pet": "Тваринка",
            "diagnosis": "Діагноз",
            "recommendation": "Рекомендації"
        }