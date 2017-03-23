from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
