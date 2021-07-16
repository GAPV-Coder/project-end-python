from newsletters import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/newsletters', views.NewsViewSet)
urlpatterns = router.urls