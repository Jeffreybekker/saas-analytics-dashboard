from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "client", "is_active")
    list_filter = ("role", "client", "is_active")
    search_fields = ("email",)
