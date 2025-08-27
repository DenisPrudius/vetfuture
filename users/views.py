from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserUpdateForm
from users.models import Doctor
from pet.models import Pet, Operation



def index(request):
    return render(request, "base.html")


class DoctorDashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "users/doctor_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        doctor = self.request.user.doctors.first()
        context["doctor"] = doctor
        context["users"] = User.objects.all()

        user_id = self.request.GET.get("user_id")
        if user_id:
            selected_user = User.objects.get(id=user_id)
            context["selected_user"] = selected_user
            context["pets"] = Pet.objects.filter(owner_id=user_id)

            if doctor:
                context["operations"] = Operation.objects.filter(doctors=doctor).order_by("-date")
            else:
                context["operations"] = Operation.objects.none()
        return context

    def test_func(self):
        return hasattr(self.request.user, "doctor")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.doctors.exists():
            return reverse("users:doctor-dashboard")
        return reverse("users:profile")


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "users/user_detail.html"
    success_url = reverse_lazy("users:user-detail")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pets"] = Pet.objects.filter(owner=self.request.user)
        return context


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:profile")


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user





