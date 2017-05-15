import unittest
from allo.allo import Dojo


class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.all_rooms)
        blue_office = my_dojo.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_added(self):
        my_dojo = Dojo()
        self.assertFalse('Red' in my_dojo.all_rooms)
        my_dojo.create_room('Red', 'office')
        self.assertTrue('Red' in my_dojo.all_rooms)


class TestAddPerson(unittest.TestCase):
    def test_add_person_successfully(self):
        my_dojo = Dojo()
        initial_persons_count = len(my_dojo.all_persons)
        my_dojo.add_person('Mike', 'fellow')
        new_persons_count = len(my_dojo.all_persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_room_added(self):
        my_dojo = Dojo()
        self.assertFalse('Fred' in my_dojo.all_persons)
        my_dojo.add_person('Fred', 'fellow')
        self.assertTrue('Fred' in my_dojo.all_persons)
