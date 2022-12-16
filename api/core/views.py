from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Question
from core.serializers import QuestionSerialazer


class QuestionAPIView(APIView):
    def get(self, request):
        lst = Question.objects.all()
        return Response({'lst': QuestionSerialazer(lst, many=True).data})

    def post(self, request):
        serialazer = QuestionSerialazer(data=request.data)
        serialazer.is_valid(raise_exception=True)
        serialazer.save()
        return Response({"post": serialazer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "method PUT not allolwed!"})

        try:
            instance = Question.objects.get(pk=pk)
        except:
            return Response({"error": "Obj doesn't exists"})

        serialazer = QuestionSerialazer(data=request.data, instance=instance)
        serialazer.is_valid(raise_exception=True)
        serialazer.save()
        return Response({"post": serialazer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "method DELETE not allolwed!"})
        try:
            Question.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Obj doesn't exists"})

        return Response({"message": f"question id: {pk} has delete"})

