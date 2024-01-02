from django.urls import path
from .views import add_member, add_community_task, show_communities, create_community, view_community, \
    get_member_adder, update_community, view_community_task, update_community_task, delete_community_task

urlpatterns = [
    path("communities", show_communities, name="communities"),
    path("create_community", create_community, name="create_community"),
    path("view_community/<str:pk>", view_community, name="view_community"),
    path("member_adder/<str:pk>", get_member_adder, name="member_adder"),
    path("add_member/<str:cid>/<str:uid>", add_member, name="add_member"),
    path("update_community/<str:pk>", update_community, name="update_community"),
    path("add_community_task/<str:pk>", add_community_task, name="add_community_task"),
    path("view_community_task/<str:pk>", view_community_task, name="view_community_task"),
    path("update_community_task/<str:pk>", update_community_task, name="update_community_task"),
    path("delete_community_task/<str:pk>", delete_community_task, name="delete_community_task"),
]