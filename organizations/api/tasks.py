from celery import shared_task
from django.db.transaction import atomic
from datetime import datetime, date
from api.models import ChessGame, CompetitionResult
from random import randint


@shared_task
def simulate_playing():
    """Simulates an organization that organizes playing chess-games between players
    according to the games those have not been played yet"""
    not_played_games = ChessGame.objects.filter(state="not-played")
    for game in not_played_games:
        players = (game.white, game.black)
        with atomic():
            CompetitionResult.objects.create(winner_id=players[randint(0, 1)],
                                             match=ChessGame.objects.get(_id=game._id))
            match = ChessGame.objects.get(_id=game._id)
            match.state = "played"
            match.save()


@shared_task
def organize():
    """Organizes new matches between winners"""
    be_played = CompetitionResult.objects.all()
    player_pairs = [i for i in zip(be_played[::2], be_played[1::2])]
    for w, b in player_pairs:
        with atomic():
            local_date = datetime.now()
            ChessGame.objects.create(white=w.winner_id,
                                     black=b.winner_id,
                                     competition_date=date(year=local_date.year,
                                                           month=local_date.month,
                                                           day=local_date.day + 10))
