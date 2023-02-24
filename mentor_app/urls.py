from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('onboarding/', views.OnboardingView.as_view()),
    path('registration/', views.RegistrationView.as_view()),
    path('auth/', include('rest_framework.urls'))

]
