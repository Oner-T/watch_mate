from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-details')
    
]