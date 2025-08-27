from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import PetHealthInfoCreateForm
from .models import PetHealthInfo, Doctor, Pet

class PetHealthInfoCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = PetHealthInfo
    form_class = PetHealthInfoCreateForm
    template_name = "health/pet_health_form.html"
    success_url = reverse_lazy("users:doctor-dashboard")

    def form_valid(self, form):
        form.instance.doctor = Doctor.objects.get(user=self.request.user)
        return super().form_valid(form)

    def test_func(self):
        return hasattr(self.request.user, "doctors")


class PetHealthDeleteView(generic.DeleteView):
    model = PetHealthInfo
    template_name = "health/pet_health_confirm_delete.html"
    success_url = reverse_lazy("users:doctor-dashboard")

    def get_success_url(self):
        user_id = self.object.pet.owner.id
        return f"{reverse_lazy('users:doctor-dashboard')}?user_id={user_id}"


