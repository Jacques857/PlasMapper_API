from msilib.schema import Feature
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .Feature import Feature

class FeatureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 300)
    start = serializers.IntegerField()
    stop = serializers.IntegerField()
    legend = serializers.CharField(max_length = 20)

    def create(self, validated_data):
        """
        Create and return a new Feature instance, given the validated data
        """
        return Feature.object.create(**validated_data)