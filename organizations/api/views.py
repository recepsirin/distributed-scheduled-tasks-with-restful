from .models import ChessGame
from .serializers import GameSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView


class ChessGameView(ListAPIView, CreateAPIView, GenericAPIView):
    queryset = ChessGame.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
