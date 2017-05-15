import unittest
from allo.allo import Dojo


class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.my_dojo = Dojo

    def test_create_room_successfully(self):
        initial_room_count = len(self.my_dojo.all_rooms)
        blue_office = self.my_dojo.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_added(self):
        self.assertFalse('Red' in self.my_dojo.all_rooms)
        self.my_dojo.create_room('Red', 'office')
        self.assertTrue('Red' in self.my_dojo.all_rooms)


class TestAddPerson(unittest.TestCase):

    def setUp(self):
        self.my_dojo = Dojo

    def test_add_person_successfully(self):
        initial_persons_count = len(self.my_dojo.all_persons)
        self.my_dojo.add_person('Mike', 'fellow')
        new_persons_count = len(self.my_dojo.all_persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_person_added(self):
        self.assertFalse('Fred' in self.my_dojo.all_persons)
        self.my_dojo.add_person('Fred', 'fellow')
        self.assertTrue('Fred' in self.my_dojo.all_persons)
