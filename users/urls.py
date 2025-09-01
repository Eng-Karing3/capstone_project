from django.urls import path
from .views import RoleListCreateView, ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
