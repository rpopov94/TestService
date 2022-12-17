from django.contrib import admin
from django.urls import path

from core.views import QuestionAPIList, QuestionAPIUpdate, QuestionAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/questions/', QuestionAPIList.as_view()),
    path('api/v1/questions/<int:pk>/', QuestionAPIUpdate.as_view()),
    path('api/v1/questions/delete/<int:pk>', QuestionAPIDestroy.as_view()),
]
