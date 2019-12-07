from rest_framework import serializers
from evaluation.models import ImageOption, ImageQuestion, Test5


class ImageOptionSerializer(serializers.ModelSerializer):
    audio = serializers.SerializerMethodField('get_audio')

    class Meta:
        model = ImageOption
        fields = ['image', 'text', 'correct']

    def get_audio(self, obj):
        request = self.context.get('request')
        url = obj.audio.url
        return request.build_absolute_uri(url)

class ImageQuestionSerializer(serializers.ModelSerializer):
    options = ImageOptionSerializer(many=True)

    class Meta:
        model = ImageOption
        fields = ['text', 'options']


class Test5Serializer(serializers.ModelSerializer):
    questions = ImageQuestionSerializer(many=True)

    class Meta:
        model = Test5
        fields = ['name', 'heading', 'questions', 'subject' ]

