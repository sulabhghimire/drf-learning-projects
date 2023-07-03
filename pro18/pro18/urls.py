from django.contrib import admin
from django.urls import path, include

from api import views as api_views
from api.auth import CustomAuthToken

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


#creating a router object
router = DefaultRouter()

#register viewset with router
router.register('studentapi', api_views.StudentModelViewSet, basename='student')
# router.register('stuapi', api_views.StudentReadOnlyModelViewSet, basename='studentreadonly')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view())
    # path('gettoken/', obtain_auth_token),
]
