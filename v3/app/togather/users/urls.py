from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import set_profile, show_profile, user_login, user_logout, user_signup


urlpatterns = [
    path("signup", user_signup, name="signup"),
    path("login", user_login, name="login"),
    path("logout", user_logout, name="logout"),
    path("show_profile", show_profile, name="show_profile"),
    path("set_profile", set_profile, name="set_profile")
    ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)