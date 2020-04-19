from django.contrib import admin

try:
    from api.models import Country, City
    admin.site.register(Country)
    admin.site.register(City)
except:
    pass
