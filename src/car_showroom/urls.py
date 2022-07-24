from rest_framework import routers

from .views import CarShowroomListViewSet

router = routers.SimpleRouter()
router.register(r'customers', CarShowroomListViewSet, basename='customer')

urlpatterns = router.urls