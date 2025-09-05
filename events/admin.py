from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "user", "timestamp")
    list_filter = ("event_type", "timestamp")
    search_fields = ("user__email", "metadata")
