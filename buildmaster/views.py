from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Project, Tasks, TeamMember
from .serializers import (
    DashboardSerializer,
    ProjectSerializer,
    TaskSerializer,
    TeamMemberSerializer,
)


# PROJECT VIEWSET
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# TASK VIEWSET
class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


# TEAM MEMBER VIEWSET
class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


# DASHBOARD API
class DashboardAPIView(APIView):
    def get(self, request):
        serializer = DashboardSerializer({})
        return Response(serializer.data)
