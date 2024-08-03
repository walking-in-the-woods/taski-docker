from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
