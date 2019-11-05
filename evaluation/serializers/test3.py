from rest_framework import serializers
from evaluation.models import Test3


class Test3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test3
        fields = ['name', 'heading', ]
