from django.urls import path, include
from web_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('site', views.WebProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('qos-eval/', views.QualityApiView.as_view()),
]