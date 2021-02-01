from rest_framework import serializers
from .models import ChessGame
from django_filters.rest_framework import DjangoFilterBackend


class GameSerializer(serializers.ModelSerializer):
    filter_backends = [DjangoFilterBackend]

    class Meta:
        model = ChessGame
        fields = '__all__'
