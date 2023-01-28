from rest_framework import serializers
from core.models import Question, Test
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


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


