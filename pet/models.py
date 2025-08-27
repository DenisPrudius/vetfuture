from django.conf import settings
from django.db import models
from users.models import Doctor


class Pet(models.Model):
    nickname = models.CharField(max_length=255)
    age = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner_pet")

    def __str__(self):
        return f"{self.nickname} ({self.owner.username})"




class Operation(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name="doctor_operations")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pet_operations")
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Operation for {self.pet.nickname} on {self.date}"
