from django.db import models
import uuid

class Bin(models.Model):
    name = models.CharField(null=True, blank=True, max_length=20)
    secret = models.UUIDField(default=uuid.uuid4)
    version = models.CharField(null=False, blank=False, max_length=20)
    architecture= models.CharField(null=False, blank=False, max_length=20)
    location = models.CharField(null=False, blank=False, max_length=70)
    launch_date = models.DateTimeField(auto_now=True)
    waste_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.location} {str(self.id)}"