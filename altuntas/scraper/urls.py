# Rest Framework
from rest_framework.routers import DefaultRouter

# Applications
from scraper.views.entries import EksiSozlukEntryViewSet

router = DefaultRouter(trailing_slash=False)
router.register("entries/eksisozluk", EksiSozlukEntryViewSet, basename="list-eksisozluk-entries")

urlpatterns = router.urls
