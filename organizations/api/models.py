from django.db import models


class ChessGame(models.Model):
    _id = models.AutoField(primary_key=True)
    white = models.PositiveIntegerField(null=False)
    black = models.PositiveIntegerField(null=False)
    competition_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s vs %s >> %s" % (self.white, self.black, self.competition_date)


class CompetitionResult(models.Model):
    winner_id = models.IntegerField(null=False)
    match = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
