from django.urls import path
from .views import AnViewSet

urlpatterns = [
    path('an/', AnViewSet)
]
