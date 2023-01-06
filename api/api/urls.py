from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.views import QuestionAPIUpdate, QuestionAPIDestroy, ThemeAPIList, ThemeAPIUpdate, ThemeAPIDestroy, ProfileView, RegisterView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
    path('api/profile/', ProfileView.as_view()),
    path('api/questions/<int:pk>/', QuestionAPIUpdate.as_view()),
    path('api/questions/delete/<int:pk>', QuestionAPIDestroy.as_view()),
    path('api/themes/', ThemeAPIList.as_view()),
    path('api/themes/<int:pk>/', ThemeAPIUpdate.as_view()),
    path('api/themes/delete/<int:pk>', ThemeAPIDestroy.as_view()),
    path('api/register/', RegisterView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
