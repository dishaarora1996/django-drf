from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    # path('stream/', views.StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('<int:pk>/review/', views.ReviewListView.as_view(), name='review-list'),
    path('<int:pk>/review-create/', views.ReviewCreateView.as_view(), name='review-list'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
]