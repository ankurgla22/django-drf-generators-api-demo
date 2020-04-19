
# Django DRF Automatically Generate API

Django Rest Framework project featuring API Views, Serializers and Urls generated using drf-generators.

The tests file contains classes to generate and test each style of API.

#### Requirement
* Python3
* pip3

#### Installation

```
cd django-drf-generators-api-demo

pip3 install -r requirements.txt
```

#### Update api/model.py


```
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

        
```
 
#### Generate APIs

```
python3 manage.py generate api
```

#### Migrate DB

```
python3 manage.py makemigrations api
python3 manage.py migrate
```

#### RUN Server

```
python3 manage.py runserver 0.0.0.0:8000
```

#### Check API

```
http://127.0.0.1:8000/api/country/
```

#### Create Django Admin User

```
python3 manage.py createsuperuser

```
#### Check Django Admin Console

```
http://127.0.0.1:8000/admin/
```

That's it!
