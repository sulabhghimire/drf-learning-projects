from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),

    # path('studentapi/<int:pk>/', views.StundetRetrieveUpdate.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
]
