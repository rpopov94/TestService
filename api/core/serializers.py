from rest_framework import serializers
from core.models import Question, Test


class QuestionSerialazer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = '__all__'
        

class ThemeSerialazer(serializers.ModelSerializer):
    questions = QuestionSerialazer(many=True)
    class Meta:
        model = Test
        fields = ['name', 'questions']