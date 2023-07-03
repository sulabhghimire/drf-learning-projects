from django.contrib import admin
from django.urls import path, include

from api import views as api_views

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#creating a router object
router = DefaultRouter()

#register viewset with router
router.register('studentapi', api_views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtiain'),
    path('getrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokenverify/', TokenVerifyView.as_view(), name='token_verify'),
]

# http POST http://127.0.0.1:8000/gettoken/ username=superuser password=superuser
    # {
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDk4NDIzLCJpYXQiOjE2ODc0OTgxMjMsImp0aSI6ImY5M2RhZTFjM2ZjYTRiMmE5YTJjODcyNzk1NGUwNDIyIiwidXNlcl9pZCI6MX0.iiTMFCJC6p50jNn3tPilaEhYy6RyI1teXAddmTuLgQo",
    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzU4NDUyMywiaWF0IjoxNjg3NDk4MTIzLCJqdGkiOiI3NDk5ODE4NGNkOTc0OGM0OWFlOGE4MmZhYTdiNWM5YiIsInVzZXJfaWQiOjF9.0A4n6V-qyHotNUpzjvDazrV7JhhSYuEt8YQ9tQR0NG4"
    # }

# http POST http://127.0.0.1:8000/tokenverify/ token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDk4NDIzLCJpYXQiOjE2ODc0OTgxMjMsImp0aSI6ImY5M2RhZTFjM2ZjYTRiMmE5YTJjODcyNzk1NGUwNDIyIiwidXNlcl9pZCI6MX0.iiTMFCJC6p50jNn3tPilaEhYy6RyI1teXAddmTuLgQo'

# http POST http://127.0.0.1:8000/getrefresh/ refresh='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzU4NDUyMywiaWF0IjoxNjg3NDk4MTIzLCJqdGkiOiI3NDk5ODE4NGNkOTc0OGM0OWFlOGE4MmZhYTdiNWM5YiIsInVzZXJfaWQiOjF9.0A4n6V-qyHotNUpzjvDazrV7JhhSYuEt8YQ9tQR0NG4'