from django.urls import path, include
from . import routers, views

urlpatterns = [
    path('data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),  # get data for the currently logged in user
    path('users/', include(routers.router.urls)),
]