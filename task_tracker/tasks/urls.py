from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('Taskc', TaskViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls