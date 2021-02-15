from django.db import models

STATES = (("not-played", "NOT PLAYED"), ("playing", "PLAYING"), ("played", "PLAYED"))


class ChessGame(models.Model):
    _id = models.AutoField(primary_key=True)
    white = models.PositiveIntegerField(null=False)
    black = models.PositiveIntegerField(null=False)
    competition_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)
    state = models.CharField(choices=STATES, max_length=15, default="not-played", null=False)

    def __str__(self):
        return "%s vs %s >> %s" % (self.white, self.black, self.competition_date)

    class Meta:
        unique_together = ('white', 'black')


class CompetitionResult(models.Model):
    winner_id = models.PositiveIntegerField(null=False)
    match = models.ForeignKey(ChessGame, on_delete=models.CASCADE)
