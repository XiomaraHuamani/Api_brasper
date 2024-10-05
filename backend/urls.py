from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("apps.users.urls")),
    path('api/v1/auth/', include('apps.social_accounts.urls')),
    path('api/v1/coin/', include('apps.coin.urls'))
]
