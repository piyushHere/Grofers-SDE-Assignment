from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('lucky_draw/', include('lucky_draw.urls')),
    path('admin/', admin.site.urls),
]
