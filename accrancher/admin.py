from django.contrib import admin

# Register your models here.
from .models import UserProfile, SaveChkbox
admin.site.register(UserProfile)
admin.site.register(SaveChkbox)