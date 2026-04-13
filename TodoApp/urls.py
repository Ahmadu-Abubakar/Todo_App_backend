from django.urls import path
from.views import *
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
routers.register('tasks', TaskViewSet)


urlpatterns = [
    path("register/", RegisterView.as_view())
    # path('tasks/', TaskList.as_view()),
    # path('tasks/<int:pk>/', TaskDetails.as_view())
]

urlpatterns += routers.urls