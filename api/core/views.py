from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from core.models import Question, Test
from core.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from core.serializers import (
                                QuestionSerialazer,
                                ThemeSerialazer,
                                UserSerializer,
                                AnswerSerialazer,
                                CustomUserRetrieveSerializer,
                                ThemeNameListSerialazer,
                                TestStatistik
                            )
from rest_framework import permissions
from rest_framework.response import Response


CustomUser = get_user_model()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    **GET:** List details for a ``CustomUser``.

    **PUT:** Update details of a ``CustomUser``.

    **DELETE:** Delete a specific ``CustomUser``.

    This view can be used to retrieve data for the current logged in user.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class QuestionsPagList(PageNumberPagination):
    page_size = 9
    page_query_param = 'page_size'
    max_page_size = 100

class QuestionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsOwnerOrReadOnly, )


class QuestionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsAdminOrReadOnly, )

class ThemeAPIList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeNameListSerialazer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = QuestionsPagList


class ThemeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
    permission_classes = (IsOwnerOrReadOnly, )


class ThemeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
    permission_classes = (IsAdminOrReadOnly, )
    
class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })

class GetAnswersView(generics.RetrieveUpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = AnswerSerialazer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = QuestionsPagList

class TestStatistickView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestStatistik