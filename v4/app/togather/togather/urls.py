from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('', include('landing.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    path('friends/', include('friends.urls')),
    path('api/', include('tasks.api.urls')),
    path('api/', include('users.api.urls'))

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)