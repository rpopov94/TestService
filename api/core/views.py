from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Question
from core.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from core.serializers import QuestionSerialazer


class QuestionsPagList(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 1000

class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = QuestionsPagList


class QuestionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsOwnerOrReadOnly, )


class QuestionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsAdminOrReadOnly, )
