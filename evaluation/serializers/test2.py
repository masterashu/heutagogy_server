from rest_framework import serializers
from evaluation.models import Test2, PictureDescriptionPair


class PictureDescriptionPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureDescriptionPair
        fields = ['picture', 'description', ]


class Test2Serializer(serializers.ModelSerializer):
    pictures = PictureDescriptionPairSerializer(many=True)
    
    class Meta:
        model = Test2
        fields = ['name', 'heading', 'pictures', ]
