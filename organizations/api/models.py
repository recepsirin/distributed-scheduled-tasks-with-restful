from django.db import models


class ChessGame(models.Model):
    _id = models.AutoField(primary_key=True)
    white = models.IntegerField(null=False)
    black = models.IntegerField(null=False)
    competition_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)


class CompetitionResult(models.Model):
    winner_id = models.IntegerField(null=False)
    match = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
