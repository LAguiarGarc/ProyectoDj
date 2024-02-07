from django.urls import path, include
from rest_framework import routers
from Tasks import views

router= routers.DefaultRouter()
router.register(r'Tasks', views.Tasksvi,'Tasks')
urlpatterns=[
    path('api/v1/', include(router.urls) )
]
