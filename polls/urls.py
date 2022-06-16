from django.urls import path, include

from .views import main, ContentView, SingleContentView, CreateContentView, AddComment

urlpatterns = [
    path('', ContentView.as_view(), name='polls'),
    path('<str:slug>/', SingleContentView.as_view(), name='single'),
    path('add/', CreateContentView.as_view(), name='add'),
    path('review/<int:pk>', AddComment.as_view(), name='comment'),
]
