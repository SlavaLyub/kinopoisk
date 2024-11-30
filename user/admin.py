from django.contrib import admin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'avatar_image']

    def avatar_image(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{0}" style="width: 50px; height: 50px;" />'.format(
                    obj.avatar.url))
        else:
            return 'No image'

    avatar_image.short_description = 'Avatar'
