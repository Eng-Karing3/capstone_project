from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "status", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("status", "created_at")

# Register your models here.
