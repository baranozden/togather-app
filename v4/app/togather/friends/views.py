from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from users.models import Profile
from .models import FriendRequest, Friendship
from typing import Dict, List


User = get_user_model()


def get_friends(request) -> List[User]:
    """
    Retrieves a list of friends for the currently logged-in user.

    params:
        request: The HTTP request object containing user information.

    returns:
        A list of User objects representing the user's friends.
    """
    user_friendships = Friendship.objects.filter(
        Q(user1=request.user, is_active=True) | Q(user2=request.user, is_active=True)
    )
    friends = []
    for friendship in user_friendships:
        if friendship.user1 == request.user:
            friends.append(friendship.user2)
        else:
            friends.append(friendship.user1)
    return friends


def get_pending_requests(request) -> Dict[str, List[User]]:
    """
    Fetches information about pending friend requests for the logged-in user.

    params:
        request: The HTTP request object containing user information.

    returns:
        A dictionary with two keys:
            - 'sent': A list of User objects representing users the current user has sent pending friend requests to.
            - 'received': A list of User objects representing users sent pending friend requests to the current user.
    """
    sent_pending_requests = FriendRequest.objects.filter(
        Q(sender=request.user, status="pending")
    )
    received_pending_requests = FriendRequest.objects.filter(
        Q(receiver=request.user, status="pending")
    )
    sent_pending = [pending.receiver for pending in sent_pending_requests]
    received_pending = [pending.sender for pending in received_pending_requests]
    return {"sent": sent_pending, "received": received_pending}


def concat_user_credentials(profile) -> str:
    """
    Combines the username, first name, and last name of a user profile into a single string.

    params:
        profile: A Profile object representing a user.

    returns:
        A string containing the user's username, first name, and last name separated by spaces.
    """
    return str(profile.user.username) + " " + str(profile.user.first_name) + " " + str(profile.user.last_name)


@login_required(login_url="/users/login")
def browse_profiles(request) -> render:
    """
    Renders the page for browsing user profiles, excluding friends, the logged-in user.

    params:
        request: The HTTP request object containing user information.

    returns:
        A Django render object with context data for the "friends/profile_browser.html" template.
    """
    excluded = get_friends(request)  # Exclude friends
    excluded += [request.user]  # Exclude the logged in user
    pendings = get_pending_requests(request)
    profiles = Profile.objects.exclude(user__in=excluded)
    search_query = request.GET.get('search')

    if search_query:
        profiles = [profile for profile in profiles if search_query.lower() in concat_user_credentials(profile)]
    context = {
        "profiles": profiles,
        "pendings_sent": pendings["sent"],
        "pendings_received": pendings["received"]
    }
    return render(request, "friends/profile_browser.html", context)


@login_required(login_url="/users/login")
def show_user_profile(request, pk) -> render:
    """
    Renders the page for a specific user profile, including friend status and pending request information.

    params:
        request: The HTTP request object containing user information.
        pk: The primary key of the user profile to display.

    returns:
        A Django HttpResponse object with context data for the "friends/profile_page.html" template.
    """
    friends = get_friends(request)
    pending_requests = get_pending_requests(request)
    profile = Profile.objects.get(id=pk)
    status = None

    if profile.user in friends:
        status = "friend"
    else:
        if profile.user in pending_requests["sent"]:
            status = "pending_sent"
        elif profile.user in pending_requests["received"]:
            status = "pending_received"

    context = {
        "profile": profile,
        "status": status
    }
    return render(request, "friends/profile_page.html", context)


@login_required(login_url="/users/login")
def send_request(request, pk) -> redirect:
    """
    Sends a friend request to another user or updates an existing pending request.

    params:
        request: The HTTP request object containing user information.
        pk: The primary key of the user to send the request to.

    returns:
        A Django redirect object back to the previously visited page.
    """
    user = User.objects.get(pk=pk)
    if user != request.user:
        if FriendRequest.objects.filter(sender=request.user, receiver=user).exists():
            existing_request = FriendRequest.objects.get(sender=request.user, receiver=user)
            existing_request.status = "pending"
            existing_request.save()
        else:
            FriendRequest.objects.create(sender=request.user, receiver=user)
        profile = Profile.objects.get(user=user)
    return redirect(request.META.get('HTTP_REFERER', f"/show_other_profile/{profile.id}"))


@login_required(login_url="/users/login")
def cancel_request(request, user_id) -> redirect:
    """
    Cancels a pending friend request sent to another user.

    params:
        request: The HTTP request object containing user information.
        user_id: The user ID of the receiver of the friend request to cancel.

    returns:
        A Django redirect object back to the previously visited page.
    """
    friend_request = FriendRequest.objects.get(sender=request.user, receiver=user_id)
    friend_request.status = "cancelled"
    friend_request.save()
    profile = Profile.objects.get(user=user_id)
    return redirect(request.META.get('HTTP_REFERER', f"/show_other_profile/{profile.id}"))


@login_required(login_url="/users/login")
def accept_request(request, sender) -> redirect:
    """
    Accepts a pending friend request from another user.

    params:
        request: The HTTP request object containing user information.
        sender: Username of the user who sent the friend request.

    returns:
        A Django redirect object back to the "show_activities" page.
    """
    sender_user = User.objects.get(username=sender)
    friend_request = FriendRequest.objects.get(sender=sender_user, receiver=request.user)
    friend_request.status = "accepted"
    friend_request.save()
    Friendship.objects.create(
        user1=sender_user,
        user2=request.user,
        is_active=True
    )
    return redirect("show_activities")


@login_required(login_url="/users/login")
def reject_request(request, sender) -> redirect:
    """
    Rejects a pending friend request from another user.

    params:
        request: The HTTP request object containing user information.
        sender: Username of the user who sent the friend request.

    returns:
        A Django redirect object back to the "show_activities" page.
    """
    sender_user = User.objects.get(username=sender)
    friend_request = FriendRequest.objects.get(sender=sender_user, receiver=request.user)
    friend_request.status = "rejected"
    friend_request.save()
    return redirect("show_activities")


@login_required(login_url="/users/login")
def remove_friend(request, friend) -> redirect:
    """
    Removes a friend from the current user's friend list.

    params:
        request: The HTTP request object containing user information.
        friend: Username of the friend to remove.

    returns:
        A redirect object back to the "friends/show_friends" page if the request is POST,
        or a render object with friend information for confirmation if the request is GET.
    """
    friend_user = User.objects.get(username=friend)
    friendship = Friendship.objects.get(
        Q(user1=request.user, user2=friend_user, is_active=True) | Q(user1=friend_user, user2=request.user,
                                                                     is_active=True)
    )
    if request.method == "POST":
        # friendship.is_active = False
        friendship.delete()
        return redirect("/friends/show_friends")

    context = {"friend": friend_user}
    return render(request, "friends/confirm_delete.html", context)


@login_required(login_url="/users/login")
def show_activities(request) -> render:
    """
    Renders the page for displaying friendship requests.

    params:
        request: The HTTP request object containing user information.

    returns:
        A Django render object with context data for the "friends/activity.html" template.
    """
    pendings = get_pending_requests(request)["received"]
    pendings = Profile.objects.filter(user__in=pendings)
    context = {
        "pendings": pendings
    }
    return render(request, "friends/activity.html", context)


@login_required(login_url="/users/login")
def show_friends(request) -> render:
    """
    Renders the page for displaying a list of the current user's friends.

    params:
        request: The HTTP request object containing user information.

    returns:
        A Django render object with context data for the "friends/friends_page.html" template.
    """
    friends = get_friends(request)
    friends = Profile.objects.filter(user__in=friends)
    search_query = request.GET.get('search')
    if search_query:
        friends = [friend for friend in friends if search_query.lower() in concat_user_credentials(friend)]

    context = {
        "friends": friends
    }
    return render(request, "friends/friends_page.html", context)
