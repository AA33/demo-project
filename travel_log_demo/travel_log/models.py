from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Trip(models.Model):
    trip_name = models.CharField('Name', max_length=100)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    trip_description = models.CharField('Description', max_length=500)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.trip_name + '/' + self.user.username


class Destination(models.Model):
    destination_name = models.CharField('Name', max_length=100)

    loc_validators = [MaxValueValidator(180), MinValueValidator(-180)]
    location_lat = models.FloatField('Latitude', validators=loc_validators)
    location_long = models.FloatField('Longitude', validators=loc_validators)

    destination_description = models.CharField('Description', max_length=500)
    rating = models.IntegerField('Rating', validators=[MaxValueValidator(10), MinValueValidator(1)], default=5)
    trip = models.ForeignKey(Trip)

    def __unicode__(self):
        return self.destination_name + '/' + str(self.location_lat) + ',' + str(self.location_long) + '/' + str(
            self.rating) + '/' + self.trip.trip_name