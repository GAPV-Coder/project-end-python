from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/users', views.UserViewSet)
urlpatterns = router.urls