from rest_framework import serializers
from core.models import Question


class QuestionSerialazer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    q1 = serializers.CharField(max_length=255)
    q2 = serializers.CharField(max_length=255)
    q3 = serializers.CharField(max_length=255)
    q4 = serializers.CharField(max_length=255)
    answer = serializers.CharField(max_length=255)
    test_id = serializers.IntegerField()

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance)
        instance.q1 = validated_data.get('q1', instance)
        instance.q2 = validated_data.get('q2', instance)
        instance.q3 = validated_data.get('q3', instance)
        instance.q4 = validated_data.get('q4', instance)
        instance.answer = validated_data.get('answer', instance)
        instance.test_id = validated_data.get('test_id', instance)
        instance.save()
        return instance

