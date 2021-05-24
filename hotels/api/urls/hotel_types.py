from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views.views import HotelTypeViewSets

router = DefaultRouter()

router.register("hotel-types", HotelTypeViewSets)


urlpatterns = router.urls
