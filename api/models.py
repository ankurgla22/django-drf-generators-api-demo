from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64)
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'country'

class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'city'
