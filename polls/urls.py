from django.urls import path, include

from .views import main, ContentView, SingleContentView, CreateContentView, AddComment, TagContentView, CategoryContentView

urlpatterns = [
    path('', ContentView.as_view(), name='polls'),
    path('add/', CreateContentView.as_view(), name='add'),
    path('<str:slug>/', SingleContentView.as_view(), name='single'),
    path('category/<str:slug>', CategoryContentView.as_view(), name='category'),
    path('tag/<str:slug>', TagContentView.as_view(), name='tag'),
    path('review/<int:pk>', AddComment.as_view(), name='comment'),
]
