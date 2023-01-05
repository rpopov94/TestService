from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Question, Test
from core.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from core.serializers import QuestionSerialazer, ThemeSerialazer


class QuestionsPagList(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 100

class QuestionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    # permission_classes = (IsOwnerOrReadOnly, )


class QuestionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    # permission_classes = (IsAdminOrReadOnly, )

class ThemeAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = QuestionsPagList


class ThemeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
    # permission_classes = (IsOwnerOrReadOnly, )


class ThemeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
    # permission_classes = (IsAdminOrReadOnly, )


