from django.contrib import admin
from .models import CustomUser, ConfirmationCode

# Register your models here.

admin.site.register([CustomUser, ConfirmationCode])