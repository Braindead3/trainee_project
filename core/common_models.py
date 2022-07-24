from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
