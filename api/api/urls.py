from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from core.views import QuestionAPIList, QuestionAPIUpdate, QuestionAPIDestroy
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/questions/', QuestionAPIList.as_view()),
    path('api/v1/questions/<int:pk>/', QuestionAPIUpdate.as_view()),
    path('api/v1/questions/delete/<int:pk>', QuestionAPIDestroy.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
