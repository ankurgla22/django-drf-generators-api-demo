from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'country', views.CountryViewSet, 'Country')
router.register(r'city', views.CityViewSet, 'City')

urlpatterns = router.urls
