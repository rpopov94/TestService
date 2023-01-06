from rest_framework import serializers
from core.models import Question, Test
from django.contrib.auth.models import User


class QuestionSerialazer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = '__all__'
        

class ThemeSerialazer(serializers.ModelSerializer):
    questions = QuestionSerialazer(many=True)
    class Meta:
        model = Test
        fields = ['id', 'name', 'questions']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'