from django.db.models import Sum
from rest_framework import serializers

from .models import Project, Tasks, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=TeamMember.objects.all())

    team = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TeamMember.objects.all()
    )

    class Meta:
        model = Project
        fields = "__all__"


class DashboardSerializer(serializers.Serializer):
    total_projects = serializers.SerializerMethodField()
    active_projects = serializers.SerializerMethodField()
    delayed_projects = serializers.SerializerMethodField()
    active_sites = serializers.SerializerMethodField()
    total_budget = serializers.SerializerMethodField()
    total_team_members = serializers.SerializerMethodField()
    project_progress = serializers.SerializerMethodField()

    def get_total_projects(self, obj):
        return Project.objects.count()

    def get_active_projects(self, obj):
        return Project.objects.filter(status="active").count()

    def get_delayed_projects(self, obj):
        return Project.objects.filter(status="delayed").count()

    def get_active_sites(self, obj):
        return Project.objects.values("location").distinct().count()

    def get_total_budget(self, obj):
        return Project.objects.aggregate(total=Sum("budget"))["total"] or 0

    def get_total_team_members(self, obj):
        return TeamMember.objects.count()

    def get_project_progress(self, obj):
        return [
            {"month": "Jan", "planned": 10, "actual": 8},
            {"month": "Feb", "planned": 20, "actual": 18},
            {"month": "Mar", "planned": 30, "actual": 28},
        ]
