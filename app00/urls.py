from django.urls import path
from .views import PersonApi


urlpatterns = [
    path('api', PersonApi.as_view()),
]