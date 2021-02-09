from .models import ChessGame
from .serializers import GameSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, UpdateAPIView
from .pagination import Pagination


class ChessGameView(ListAPIView, CreateAPIView, UpdateAPIView, GenericAPIView):
    filter_fields = ('white', 'black', 'competition_date')
    queryset = ChessGame.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = Pagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
