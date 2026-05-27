from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ("planning", "Planning"),
        ("active", "Active"),
        ("delayed", "Delayed"),
        ("completed", "Completed"),
    ]
    TYPE_CHOICES = [
        ("commercial", "Commercial"),
        ("residential", "Residential"),
        ("infrastructure", "Infrastructure"),
        ("industrial", "Industrial"),
    ]
    title = models.CharField(unique=True, max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    client = models.CharField(max_length=150)
    location = models.CharField(max_length=200)

    manager = models.ForeignKey(
        "TeamMember",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_projects",
    )

    start_date = models.DateField()
    deadline = models.DateField()

    project_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    progress = models.PositiveIntegerField(default=0)

    budget = models.IntegerField()
    expenses = models.IntegerField()

    team = models.ManyToManyField("TeamMember", related_name="projects")

    delayed_issues = models.IntegerField()

    def __repr__(self):
        return self.title


class TeamMember(models.Model):
    TITLE_CHOICE = [
        ("project manager", "Project Manager"),
        ("contractor", "Contractor"),
        ("supervisor", "Supervisor"),
        ("site engineer", "Site Engineer"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=30, choices=TITLE_CHOICE)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="tasks"
    )
    DIFFICULTY_CHOICES = [("low", "Low"), ("medium", "Medium"), ("high", "High")]
    STATUS_CHOICES = [
        ("completed", "Complete"),
        ("pending", "Pending"),
        ("in progress", "In Progress"),
        ("blocked", "Blocked"),
        ("under review", "Under Review"),
    ]

    title = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=40, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")
    due_date = models.DateField()

    def __str__(self):
        return self.title
