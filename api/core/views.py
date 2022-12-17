from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Question
from core.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from core.serializers import QuestionSerialazer


class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class QuestionAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsOwnerOrReadOnly, )


class QuestionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer
    permission_classes = (IsAdminOrReadOnly, )
