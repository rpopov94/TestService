from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Question, Test
from core.serializers import QuestionSerialazer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialazer

    @action(methods=['GET', 'POST', 'PUT', 'DELETE'], detail=True)
    def test(self, request, pk=None):
        test = Test.objects.get(pk=pk)
        return Response({'tests': test.title})

    @action(methods=['GET'], detail=False)
    def tests(self, request):
        test = Test.objects.all()
        return Response({'tests': [t.title for t in test]})
