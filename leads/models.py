from django.db import models

class Lead(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[("new", "New"), ("contacted", "Contacted"), ("converted", "Converted")],
        default="new"
    )

    def __str__(self):
        return self.full_name

# Create your models here.
