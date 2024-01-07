from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name="album_list"),
    path('add/', views.AddAlbumCreateView.as_view(), name="add_album"),
    path('edit/<int:album_id>/', views.EditAlbumUpdateView.as_view(), name="edit_album"),
    path('delete/<int:album_id>/',views.DeleteAlbumView.as_view(), name="delete_album"),
  
]