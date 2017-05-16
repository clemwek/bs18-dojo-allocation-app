import  unittest
from allo.room import room
from allo.person import person


class TestRoom(unittest.TestCase):
    def test_can_be_created(self):
        new_room = room.Room()
        self.assertIsInstance(new_room, room.Room)

    def test_capacity(self):
        office = room.Room(4)
        living_space = room.Room(6)
        self.assertEqual(office.capacity, 4)
        self.assertEqual(living_space.capacity, 6)

    def test_occupants(self):
        fellow = person.Fellow()
        staff =person.Staff()


class TestOffice(unittest.TestCase):
    def test_add_office(self):
        office = room.Office()
        new_office = office.create_office('red', 'office')
        self.assertIn('red', new_office)


class TestLivingSpace(unittest.TestCase):
    def test_add_living_space(self):
        lining_space = room.LivingSpace()
        new_living_space = lining_space.create_office('green', 'living')
        self.assertIn('green', new_living_space)
