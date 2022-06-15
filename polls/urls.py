from django.urls import path, include

from .views import main, ContentView, SingleContentView

urlpatterns = [
    path('', ContentView.as_view(), name='polls'),
    path('name/<str:slug>/', SingleContentView.as_view(), name='single'),
]
