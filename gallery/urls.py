from django.urls import path
from gallery.views import (
    PhotoListView, PhotoDetailView,
    PhotoCreateView, PhotoUpdateView,
    PhotoDeleteView
)

app_name = 'gallery'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/edit', PhotoUpdateView.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
]
