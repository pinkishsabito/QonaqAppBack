import uuid

from django.db import models


class TourAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'touragents'
