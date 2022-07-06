from django.urls import path

from authapp.views import (
    AuthView
)

urlpatterns = [
    path('', AuthView.as_view(), name="home")
]
