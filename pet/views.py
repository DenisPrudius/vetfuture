from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic

from pet.forms import OperationForm, PetForm
from pet.models import Pet, Operation


class PetListView(generic.ListView):
    model = Pet
    template_name = "pets/pet_list.html"


class PetDetailView(generic.DetailView):
    model = Pet
    template_name = "pets/pet_detail.html"


class PetCreateView(generic.CreateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pet_form.html"
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class PetUpdateView(generic.UpdateView):
    model = Pet
    fields = "__all__"
    template_name = "pets/pet_form.html"
    success_url = reverse_lazy("pet-list")


class PetDeleteView(generic.DeleteView):
    model = Pet
    template_name = "pets/pet_confirm_delete.html"
    success_url = reverse_lazy("users:profile")


class OperationListView(generic.ListView):
    model = Operation
    template_name = "operations/operation_list.html"
    context_object_name = "operations"
    paginate_by = 10

    def get_queryset(self):
        doctor = self.request.user.doctors.first()
        if doctor:
            return Operation.objects.filter(doctors=doctor).order_by("-date")
        return Operation.objects.none()
class OperationDetailView(generic.DetailView):
    model = Operation
    template_name = "operations/operation_detail.html"
    context_object_name = "operation"

class OperationCreateView(generic.CreateView):
    model = Operation
    form_class = OperationForm
    template_name = "operations/operation_form.html"
    success_url = reverse_lazy("pet:operation-list")

class OperationUpdateView(generic.UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = "operations/operation_form.html"
    success_url = reverse_lazy("pet:operation-list")

class OperationDeleteView(generic.DeleteView):
    model = Operation
    template_name = "operations/operation_confirm_delete.html"
    success_url = reverse_lazy("pet:operation-list")