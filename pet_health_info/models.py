from django.db import models
from users.models import Doctor
from pet.models import Pet

class PetHealthInfo(models.Model):
    recommendation = models.TextField()
    diagnosis = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pet_info")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="doctor_info")

    def __str__(self):
        return f"{self.pet.nickname} - {self.diagnosis}"
