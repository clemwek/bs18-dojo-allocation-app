import  unittest
from allo.room.room import Room, Office, LivingSpace


class TestRoom(unittest.TestCase):
    def test_can_be_created(self):
        new_office = Office('Mango')
        new_living_space = LivingSpace('Banana')
        self.assertIsInstance(new_office, Office)
        self.assertIsInstance(new_living_space, LivingSpace)
