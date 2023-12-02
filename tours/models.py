import uuid

from django.db import models

from touragents.models import TourAgent


class Tour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_agent = models.ForeignKey(TourAgent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tours'
