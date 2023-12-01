from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/')
    location_coordinate = models.CharField(max_length=255)
    rating = models.FloatField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class TourAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_agent = models.ForeignKey(TourAgent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
