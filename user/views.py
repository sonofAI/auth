from rest_framework import viewsets, status, views
from rest_framework.response import Response
from .serializers import UserSerializer
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser, ConfirmationCode
from django.shortcuts import get_object_or_404

# Create your views here.

class RegistrationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        confirmation_code = ''.join(random.choices(['1','2','3','4','5','6','7','8','9','0'], k=5))
        subject = 'Confirmation Code'
        message = f'Code: {confirmation_code}'
        from_email = settings.EMAIL_HOST_USER
        receiver = [email]
        send_mail(subject, message, from_email, receiver, fail_silently=False)

        ConfirmationCode.objects.create(email=email, code=confirmation_code)

        return Response({'detail': 'Confirmation email sent.'}, status=status.HTTP_200_OK)


class ConfirmationView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        confirmation_code = request.data.get('confirmation_code')

        code = get_object_or_404(ConfirmationCode, email=email, code=confirmation_code)

        user = CustomUser(email=email)
        user.set_password(request.data.get('password'))
        user.save()

        code.delete()

        return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)