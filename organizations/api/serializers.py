from rest_framework import serializers
from .models import ChessGame, CompetitionResult
from django_filters.rest_framework import DjangoFilterBackend


class GameSerializer(serializers.ModelSerializer):
    filter_backends = [DjangoFilterBackend]

    class Meta:
        model = ChessGame
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionResult
        fields = '__all__'
