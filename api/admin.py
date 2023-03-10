from django.contrib import admin
from .models import Image, UserProfile

admin.site.register(UserProfile)
admin.site.register(Image)