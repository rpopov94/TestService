from rest_framework import serializers, validators
from core.models import Question, Test, CustomUser
from django.contrib.auth.models import User



class CustomUserSerializer(serializers.ModelSerializer):
    """
    We use this serializer for user registration. Most of the fields have
    `required=False`, but can be configured as needed. This serializer is used
    in `accounts.viewsets.CustomUserModelViewSet`.
    """

    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password', 'bio', 'gender', 'birth_date')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    """
    We use this serializer to retrieve data of the currently logged in user.
    It is used in `accounts.views.UserRetrieveUpdateDestroyAPIView`
    """
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date', 'id')



class QuestionSerialazer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = ('title', 'q1', 'q2', 'q3', 'q4', 'user')
        

class ThemeSerialazer(serializers.ModelSerializer):
    questions = QuestionSerialazer(many=True)
    class Meta:
        model = Test
        fields = ('id', 'name', 'questions')

class ThemeNameListSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'descriptor')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ASerialazer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = ('answer',)


class AnswerSerialazer(serializers.ModelSerializer):
    questions = ASerialazer(many=True)
    class Meta:
        model = Test
        fields = ('id', 'name', 'questions')


