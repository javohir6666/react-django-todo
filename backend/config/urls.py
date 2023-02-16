from django.contrib import admin
from django.urls import path, include
from todo.views import TodoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TodoView, 'task')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
