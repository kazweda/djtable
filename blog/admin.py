from django.contrib import admin
from .models import Post # 追加

class BlogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Post, BlogAdmin) # 追加