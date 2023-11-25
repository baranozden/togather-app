from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    countries = {
        "options": [
            ("turkey", "Turkey")
        ],
        "default": "turkey"
    }
    cities = {
        "options": [
            ("ankara", "Ankara")
        ],
        "default": "ankara"
    }
    interests = {
        "options": [
            ("none", "None"),
            ("music", "Music"),
            ("theatre", "Theatre"),
            ("movies", "Movies"),
            ("literacy", "Literacy")
        ],
        "default": "none"
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    bio = models.CharField(max_length=128, blank=True)
    picture = models.ImageField(
        upload_to="profile_pictures",
        default="blank-profile-picture.jpg"
    )
    country = models.CharField(
        choices=countries["options"],
        default=countries["default"],
        max_length=64
    )
    city = models.CharField(
        choices=cities["options"],
        default=cities["default"],
        max_length=64
    )
    interest = models.CharField(
        choices=interests["options"],
        default=interests["default"],
        max_length=64
    )

    def __str__(self):
        return self.user.username