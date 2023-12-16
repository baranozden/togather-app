from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    path('friends/', include('friends.urls'))

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)