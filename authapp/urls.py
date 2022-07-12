from django.urls import path

from authapp.views import (
    IndexView
)

urlpatterns = [
    path('', IndexView.as_view(), name="home")
]
