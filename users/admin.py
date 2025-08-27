from django.contrib import admin

from pet_health_info.models import PetHealthInfo
from pet.models import Pet, Operation, Doctor
admin.site.register(Pet)
admin.site.register(Operation)
admin.site.register(Doctor)
admin.site.register(PetHealthInfo)