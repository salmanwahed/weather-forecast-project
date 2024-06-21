from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


# Create your models here.
class UserQuery(models.Model):
    class DetailingType(models.TextChoices):
        CURRENT = 'current'
        MINUTELY = 'minutely'
        HOURLY = 'hourly'
        DAILY = 'daily'

    lat = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Latitude')
    lon = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Longitude')
    detailing_type = models.CharField(max_length=10, choices=DetailingType.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class OpenWeatherMapData(models.Model):
    lat = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Latitude')
    lon = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Longitude')
    timestamp = models.DateTimeField()
    response = models.TextField()

    def is_old_data(self):
        cache_over_time = timezone.now() - timedelta(minutes=settings.CACHE_TIME_IN_MINUTES)
        return self.timestamp < cache_over_time

    class Meta:
        unique_together = ['lat', 'lon']
