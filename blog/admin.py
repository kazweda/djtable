from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
User = settings.AUTH_USER_MODEL
from .models import Post

admin.site.register(Post)