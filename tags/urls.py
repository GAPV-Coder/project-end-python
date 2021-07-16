from tags import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/tags', views.TagViewSet)
urlpatterns = router.urls