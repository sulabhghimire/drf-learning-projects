from django.contrib import admin
from django.urls import path, include

from api import views as api_views

from rest_framework.routers import DefaultRouter

#creating a router object
router = DefaultRouter()

#register viewset with router
router.register('studentapi', api_views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
