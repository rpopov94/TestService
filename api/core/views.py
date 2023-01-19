from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Question, Test
from core.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from core.serializers import QuestionSerialazer, ThemeSerialazer, UserSerializer, RegisterSerializer, AnswerSerialazer
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


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

class ThemeAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = ThemeSerialazer
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

class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
        })

class GetAnswersView(generics.RetrieveUpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = AnswerSerialazer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = QuestionsPagList