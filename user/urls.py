from django.urls import path, include
from rest_framework import routers


from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', include(router.urls)),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout')
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
