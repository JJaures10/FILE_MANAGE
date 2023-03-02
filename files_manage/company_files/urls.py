from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]