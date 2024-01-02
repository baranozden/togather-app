from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class FriendRequest(models.Model):
    status_options = {
        "options": [
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
            ("cancelled", "Cancelled"),
        ],
        "default": "pending"
    }

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_request_from")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_request_to")
    status = models.CharField(
        choices=status_options["options"],
        default=status_options["default"],
        max_length=9
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("sender", "receiver")


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends_from")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends_to")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user1", "user2")