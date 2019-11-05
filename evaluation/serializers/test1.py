from rest_framework import serializers
from evaluation.models import Option, Question, Test1


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['text', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'options']


class Test1Serializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test1
        fields = ['name', 'heading', 'questions', ]

