from django.contrib import admin
from django.urls import path, include

from .views import home, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', home, name='home')
]
