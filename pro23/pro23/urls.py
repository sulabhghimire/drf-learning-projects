from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('studentapi/list/', views.StudentList.as_view()),
    path('studentapi/create/', views.StudentCreate.as_view()),
    path('studentapi/list/<int:pk>/', views.StudentRetrive.as_view()),
    path('studentapi/update/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentapi/delete/<int:pk>/', views.StudentDestroy.as_view()),
]
