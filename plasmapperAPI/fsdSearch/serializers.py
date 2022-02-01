from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class FeatureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 300)
    start = serializers.IntegerField()
    stop = serializers.IntegerField()
    legend = serializers.CharField(max_length = 20)