from votes import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/votes', views.VotesViewSet)
urlpatterns = router.urls