import uuid

from django.db import models

from core.models import Category


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
    location_coordinate = models.CharField(max_length=255)
    rating = models.FloatField()
    description = models.TextField()
    tour_list = models.ManyToManyField('Tour')

    def __str__(self):
        return self.name
