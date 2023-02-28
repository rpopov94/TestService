from django.contrib import admin
from django.urls import path, include
from core.views import (
    QuestionAPIUpdate,
    QuestionAPIDestroy,
    ThemeAPIList,
    ThemeAPIUpdate,
    ThemeAPIDestroy,
    GetAnswersView,
    UserStatistikView
    )


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
    path('api/statistic/<int:id>/', UserStatistikView.as_view()),
]
