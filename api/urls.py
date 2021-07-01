from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('list/', views.PlansList.as_view()),
    path('create/', views.PlansCreate.as_view()),
    path('update/<int:pk>/', views.PlansUpdate.as_view()),
    path('delete/<int:pk>/', views.PlansDestroy.as_view()),
]
