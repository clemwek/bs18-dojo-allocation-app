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

    def test_print_room(self):
        if self.my_dojo.create_room('office', 'Mango'):
            self.my_dojo.add_person('Mike', 'staff')
            in_room = self.my_dojo.print_room('mango')
            print(in_room)
            self.assertIn('mike', in_room)

    def test_print_allocations(self):
        self.assertEqual(self.my_dojo.print_allocations(), 'There are no rooms and no allocations made yet!')
        if self.my_dojo.create_room('office', 'Mango'):
            self.my_dojo.add_person('Mike', 'staff')
            print(self.my_dojo.all_rooms['mango'].members)
            self.assertIn('mike', self.my_dojo.all_rooms['mango'].members)

    def test_unallocated(self):
        self.my_dojo.add_person('Mike', 'staff')
        self.assertFalse(self.my_dojo.all_persons['mike'].accommodation)

    def test_list_rooms(self):
        self.assertEqual(len(self.my_dojo.all_rooms), 0)
        self.my_dojo.create_room('office', 'Mango')
        self.my_dojo.create_room('living', 'Banana')
        print(self.my_dojo.all_rooms)
        self.assertIn('mango', self.my_dojo.list_rooms())
        self.assertIn('banana', self.my_dojo.list_rooms())

    def test_rand_office_gen(self):
        pass

    def test_reallocate_person(self):
        self.my_dojo.create_room('office', 'mango')
        self.my_dojo.create_room('living', 'pine')
        self.my_dojo.add_person('john doe', 'staff', 'y')
        self.my_dojo.add_person('pete bet', 'fellow', 'y')
        self.assertIn('john doe', self.my_dojo.all_rooms['mango'].members)
        self.assertIn('pete bet', self.my_dojo.all_rooms['pine'].members)
        self.my_dojo.create_room('office', 'banana')
        self.my_dojo.create_room('living', 'apple')
        self.my_dojo.reallocate_person('john doe', 'banana')
        self.my_dojo.reallocate_person('pete bet', 'apple')
        self.assertIn('john doe', self.my_dojo.all_rooms['banana'].members)
        self.assertIn('pete bet', self.my_dojo.all_rooms['apple'].members)

    def test_load_people(self):
        print_file = 'OLUWAFEMI SULE FELLOW Y \nDOMINIC WALTERS STAFF '
        f = open('test.txt', 'w')
        f.write(print_file)
        f.close()
        self.my_dojo.load_people('test.txt')
        print(self.my_dojo.all_persons.keys())
        self.assertIn('OLUWAFEMI SULE'.lower(), self.my_dojo.all_persons.keys())
