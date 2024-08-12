from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', views.StreamPlatformAV.as_view(), name='movie-detail'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('review/', views.ReviewListView.as_view(), name='review-list'),
]