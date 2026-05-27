from django.urls import include, path
from rest_framework.routers import DefaultRouter

from buildmaster.views import (
    DashboardAPIView,
    ProjectViewSet,
    TaskViewSet,
    TeamMemberViewSet,
)

router = DefaultRouter()

router.register(r"projects", ProjectViewSet, basename="projects")

router.register(r"tasks", TaskViewSet, basename="tasks")

router.register(r"team-members", TeamMemberViewSet, basename="team-members")

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", DashboardAPIView.as_view(), name="dashboard"),
]
