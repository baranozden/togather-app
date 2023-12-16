from django.urls import path
from .views import accept_request, browse_profiles, cancel_request, reject_request, remove_friend, send_request, show_activities, show_friends, show_user_profile


urlpatterns = [
    path("profiles", browse_profiles, name="browse_profiles"),
    path("profiles/<str:pk>", show_user_profile, name="show_other_profile"),
    path("send_request/<str:pk>", send_request, name="send_request"),
    path("cancel_request/<str:user_id>", cancel_request, name="cancel_request"),
    path("accept_request/<str:sender>", accept_request, name="accept_request"),
    path("reject_request/<str:sender>", reject_request, name="reject_request"),
    path("remove_friend/<str:friend>", remove_friend, name="remove_friend"),
    path("show_activities", show_activities, name="show_activities"),
    path("show_friends", show_friends, name="show_friends")
]
