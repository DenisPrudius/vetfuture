from django.urls import path
from pet.views import PetCreateView, PetListView, PetDetailView, PetUpdateView, PetDeleteView, OperationListView, \
    OperationDetailView, OperationCreateView, OperationUpdateView, OperationDeleteView

urlpatterns = [
       path("pet/", PetListView.as_view(), name="pet-list"),
       path("detail/<int:pk>/", PetDetailView.as_view(), name="pet-detail"),
       path("create/", PetCreateView.as_view(), name="pet-create" ),
       path("update/<int:pk>/", PetUpdateView.as_view(), name="pet-update"),
       path("delete/<int:pk>/", PetDeleteView.as_view(), name="pet-delete"),
       path("operation/", OperationListView.as_view(), name="operation-list"),
       path("operation/<int:pk>/", OperationDetailView.as_view(), name="operation-detail"),
       path("operation/create/", OperationCreateView.as_view(), name="operation-create"),
       path("operation/<int:pk>/update/", OperationUpdateView.as_view(), name="operation-update"),
       path("operation/<int:pk>/delete/", OperationDeleteView.as_view(), name="operation-delete"),



]

app_name = "pet"
