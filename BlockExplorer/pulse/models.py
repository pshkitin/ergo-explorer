from django.db import models
import django.utils.timezone
from django.contrib.postgres.fields import JSONField
from datetime import timedelta
# Create your models here.

class nodeListCache(models.Model):
    nodes = JSONField()
    validTill = models.DateTimeField(default=django.utils.timezone.now)