from django.urls import path

from authapp.views import (
    IndexView,
    ProfileView
)

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('profile/', ProfileView.as_view(), name="profile"),
]
