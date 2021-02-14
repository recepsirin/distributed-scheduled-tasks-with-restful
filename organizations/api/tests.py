from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ChessGame, CompetitionResult
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class ChessGameModelTest(TestCase):

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('admin@organizations.com', 'changeme')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_players_validation(self):
        """Tests that players must have their own unique ids to take place in the competition"""
        white = None
        black = 1442921
        competition_date = "2021-01-29"

        with self.assertRaises(Exception):
            ChessGame.objects.create(white=white, black=black, competition_date=competition_date)


class ChessGameEndpointTest(TestCase):

    def setUp(self):
        """Setting up the client and sample payload"""
        self.client = APIClient()

        self.chess_game = {'white': 1442921, 'black': 1442392, 'competition_date': '2021-12-31'}
        self.response = self.client.post(reverse('chess-game'), self.chess_game, format="json")

    def test_create_organization(self):
        """Test the organizations endpoint's post method by asserting http status code"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_organizations(self):
        """"Test for get request that listing organizations"""
        response = self.client.get(reverse("chess-game"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filtering_specific_organization(self):
        """Test for filtering specific organization"""
        response = self.client.get(reverse('chess-game'), kwargs={'_id': 1})
        competition_date = response.data['results'][0]['competition_date']

        self.assertEqual(competition_date, self.chess_game.get('competition_date'))


class CompetitionResultModelTest(TestCase):

    def setUp(self):
        from model_mommy import mommy
        self.chess_game = mommy.make(ChessGame)
        self.competition_result = CompetitionResult.objects.create(winner_id=12, match=self.chess_game)

    def test_validate_model(self):
        with self.assertRaises(Exception):
            CompetitionResult.objects.create(winner_id=1231, match=None)

        self.assertTrue(self.competition_result.match.white == self.chess_game.white, True)
        self.assertEqual(self.competition_result.match.black, self.chess_game.black)
        self.assertTrue(self.competition_result.match.competition_date != self.chess_game.created_date, True)