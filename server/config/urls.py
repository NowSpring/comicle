from django.contrib import admin
from django.urls import path, include

from .router import router
from apps.members.views import CustmAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', CustmAuthToken.as_view())
]

