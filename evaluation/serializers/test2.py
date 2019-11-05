from rest_framework import serializers
from evaluation.models import Test2


class Test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = ['name', 'heading', ]
