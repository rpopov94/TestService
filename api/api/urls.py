from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import (
    QuestionAPIUpdate,
    QuestionAPIDestroy,
    ThemeAPIList,
    ThemeAPIUpdate,
    ThemeAPIDestroy,
    ProfileView,
    GetAnswersView
    )
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('accounts/', include('core.urls')),
    path('', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/questions/<int:pk>/', QuestionAPIUpdate.as_view()),
    path('api/questions/delete/<int:pk>', QuestionAPIDestroy.as_view()),
    path('api/themes/', ThemeAPIList.as_view()),
    path('api/themes/<int:pk>/', ThemeAPIUpdate.as_view()),
    path('api/themes/delete/<int:pk>', ThemeAPIDestroy.as_view()),
    path('api/answers/<int:pk>/', GetAnswersView.as_view()),
]
