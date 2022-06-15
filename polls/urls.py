from django.urls import path, include

from .views import main, ContentView

urlpatterns = [
    path('', ContentView.as_view(), name='polls'),
]
