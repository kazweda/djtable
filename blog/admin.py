from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
from .models import Post # 追加
      
# class BlogAdmin(admin.ModelAdmin):
#   def get_queryset(self, request):
#       qs = super().get_queryset(request)
#       if request.user.is_superuser:
#           return qs
#       return qs.filter(author=request.user)
    

# admin.site.register(Post, BlogAdmin) # 追加