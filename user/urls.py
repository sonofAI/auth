from django.urls import path
from .views import RegistrationViewSet, ConfirmationView, register

urlpatterns = [
    path('register/', register, name='register'),
    
    path('api/register/', RegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('api/confirm/', ConfirmationView.as_view(), name='confirmation'),
]