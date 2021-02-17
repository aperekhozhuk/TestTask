from django.urls import path, include
from api import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"posts", views.PostViewSet)


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
    path("posts/<int:post_id>/like/", views.LikeView.as_view()),
]
