from rest_framework import viewsets
from core.models import Question
from core.serializers import QuestionSerialazer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer

