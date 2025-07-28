from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/habit/', include('habit.urls')),
    path('api/users/', include('users.urls')),
    path('api/tg/', include('telegram_bot.urls')),
]
