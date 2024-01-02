from django.contrib import admin
from .models import Friendship, FriendRequest


admin.site.register([Friendship, FriendRequest])
