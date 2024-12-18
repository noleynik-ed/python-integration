from django.urls import path
from choreo.views import post_payload, index

urlpatterns = [
    path('index', index, name='index'),
    path('post_payload/', post_payload, name='post_payload'),
]