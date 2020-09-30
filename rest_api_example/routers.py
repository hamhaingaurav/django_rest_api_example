from rest_framework import routers
from example.api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

# for url in router.urls:
#     print(url)