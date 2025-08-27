from django.urls.conf import path

from pet_health_info.views import PetHealthInfoCreateView, PetHealthDeleteView

urlpatterns = [
          path("health/create/", PetHealthInfoCreateView.as_view(), name="pet-health-create"),
          path("health/<int:pk>/delete/", PetHealthDeleteView.as_view(), name="pet-health-delete"),

]
app_name = "pet_health_info"
