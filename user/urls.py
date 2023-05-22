from django.urls import path
from .views import RegistrationViewSet, ConfirmationView

urlpatterns = [
    path('register/', RegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('confirm/', ConfirmationView.as_view(), name='confirmation'),
]