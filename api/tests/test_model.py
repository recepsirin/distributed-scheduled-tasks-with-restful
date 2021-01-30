import unittest
from mongoengine import connect, disconnect
from models.players import Player
import mongoengine


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_object_creating(self):
        """Test creating objects with dummy data"""
        player = Player(rank=4325, name="John Doe", level="Master", country="UK", rating=1599)
        player.save()

        self.assertEqual(player.rank, 4325)
        self.assertTrue(player.level == "Master", True)

    def test_fields_validation(self):
        """Tests whether fields are actually validated"""
        player = Player(rank=2, name="Magnus Carlsen", level="Grandmaster", country="Norway", rating=2650)
        player.save()

        with self.assertRaises(mongoengine.errors.NotUniqueError):
            """Rank field must be unique"""
            player = Player(rank=2, name="Magnus Carlsen", level="Grandmaster", country="Norway", rating=2650)
            player.save()
            self.assertEqual(Player.objects.filter(rank=2).count(), 2)

        with self.assertRaises(mongoengine.errors.ValidationError):
            """The values that level field can take are limited."""
            player = Player(rank=1, name="Garry Kasparov", level="Grand master", country="Russia", rating=2700)
            player.save()
            self.assertNotEqual(player.level, "Grandmaster")

        with self.assertRaises(mongoengine.errors.ValidationError):
            """Rating field is required"""
            player = Player(rank=3, name="Alex Martelli", level="Master", country="Brazil")
            player.save()
