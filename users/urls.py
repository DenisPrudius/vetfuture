from django.urls import path

from users.views import UserDetailView, UserUpdateView, UserRegisterView, DoctorDashboardView, CustomLoginView

urlpatterns = [
    path("doctor-dashboard/", DoctorDashboardView.as_view(), name="doctor-dashboard"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="profile_update"),
    path("profile/login/", CustomLoginView.as_view(), name="profile-login"),


]

app_name = "users"