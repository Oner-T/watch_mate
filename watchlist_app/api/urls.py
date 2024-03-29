from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewList, ReviewDetail,ReviewCreate,WatchListAV,WatchDetailAV,
                                     StreamPlatformAV,StreamPlatformDetailAV,StreamPlatformVS,UserReview)

router = DefaultRouter()
router.register('stream',StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-list')
    
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    path('reviews/<str:username>', UserReview.as_view(), name='user-review-detail'),
    
]