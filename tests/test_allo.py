import unittest
from allo.allo import Dojo


class TestDojo(unittest.TestCase):

    def setUp(self):
        self.my_dojo = Dojo()

    def test_create_room_successfully(self):
        initial_room_count = len(self.my_dojo.all_rooms)
        blue_office = self.my_dojo.create_room('office', 'Blue')
        self.assertTrue(blue_office)
        new_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_added(self):
        self.assertFalse('red' in self.my_dojo.all_rooms)
        self.my_dojo.create_room('office', 'Red')
        self.assertTrue('red' in self.my_dojo.all_rooms.keys())

    def test_add_person_successfully(self):
        initial_persons_count = len(self.my_dojo.all_persons)
        self.my_dojo.add_person('Mike', 'fellow')
        new_persons_count = len(self.my_dojo.all_persons)
        self.assertEqual(new_persons_count - initial_persons_count, 1)

    def test_person_added(self):
        self.assertFalse('mike' in self.my_dojo.all_persons)
        self.my_dojo.add_person('Mike', 'Fellow')
        self.assertTrue('mike' in self.my_dojo.all_persons.keys())

    def test_room_cant_allocated_more_than_capacity(self):
        mango = self.my_dojo.create_room('office', 'Mango')
        self.assertTrue(mango)
        self.my_dojo.allocate_person_room('Mike', 'mango')
        self.my_dojo.allocate_person_room('James', 'mango')
        self.my_dojo.allocate_person_room('penny', 'mango')
        self.my_dojo.allocate_person_room('peter', 'mango')
        self.my_dojo.allocate_person_room('Jane', 'mango')
        self.my_dojo.allocate_person_room('Robin', 'mango')
        self.my_dojo.allocate_person_room('Margret', 'mango')
        capacity = self.my_dojo.all_rooms['mango'].capacity
        members = len(self.my_dojo.all_rooms['mango'].members)
        self.assertGreater(capacity, members)
