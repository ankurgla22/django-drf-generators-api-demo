
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
from rest_framework.serializers import ModelSerializer
from api.models import Country, City


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
        
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
