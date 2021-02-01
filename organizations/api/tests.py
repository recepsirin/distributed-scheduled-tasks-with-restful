from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ChessGame


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
