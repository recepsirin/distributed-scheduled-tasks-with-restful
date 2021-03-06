# Generated by Django 3.1.5 on 2021-02-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210208_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='chessgame',
            name='state',
            field=models.CharField(choices=[('not-played', 'NOT PLAYED'), ('playing', 'PLAYING'), ('played', 'PLAYED')], default='not-played', max_length=15),
        ),
        migrations.AlterField(
            model_name='competitionresult',
            name='winner_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='chessgame',
            unique_together={('white', 'black')},
        ),
    ]
