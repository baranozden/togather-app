from django.contrib import admin
from .models import CommunityTask, Community


admin.site.register([Community, CommunityTask])
