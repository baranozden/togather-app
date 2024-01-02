from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Community(models.Model):
    users = models.ManyToManyField(User, related_name='member', blank=True)
    community_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.community_name


class CommunityTask(models.Model):
    task_types = {
        "options": [
            ("manual", "Manual"),
            ("automated", "Automated")
        ],
        "default": "manual"
    }

    priority_levels = {
        "options": [
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High")
        ],
        "default": "low"
    }

    recurrence_types = {
        "options": [
            ("none", "None"),
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly")
        ],
        "default": "none"
    }

    reminder_types = {
        "options": [
            ("none", "None"),
            ("before_15", "15 minutes before"),
            ("before_30", "30 minutes before"),
            ("before_1d", "1 Day before")
        ],
        "default": "none"
    }

    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    task_type = models.CharField(
        max_length=9,
        choices=task_types["options"],
        default=task_types["default"]
    )
    priority = models.CharField(
        max_length=6,
        choices=priority_levels["options"],
        default=priority_levels["default"]
    )
    detailed_info = models.CharField(max_length=128, blank=True)
    place = models.CharField(max_length=64, blank=True)
    attachment = models.FileField(upload_to="togather/uploads/", blank=True, null=True)
    reminder = models.CharField(
        max_length=17,
        choices=reminder_types["options"],
        default=reminder_types["default"]
    )
    recurrence = models.CharField(
        max_length=7,
        choices=recurrence_types["options"],
        default=recurrence_types["default"]
    )
    # Color and People Assignment will be added
    # color = None
    # other_people = None

    def __str__(self):
        return self.task_name

