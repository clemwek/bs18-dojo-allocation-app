import unittest
from allo.allo import Dojo


class TestDojo(unittest.TestCase):

    def setUp(self):
        self.my_dojo = Dojo()

    def test_create_room_successfully(self):
        initial_office_count = len(self.my_dojo.all_rooms['office'])
        blue_office = self.my_dojo.create_room('office', 'Blue')
        self.assertTrue(blue_office)
        new_office_count = len(self.my_dojo.all_rooms['office'])
        self.assertEqual(new_office_count - initial_office_count, 1)

    def test_room_added(self):
        self.assertFalse('red' in self.my_dojo.all_rooms['office'])
        self.my_dojo.create_room('office', 'Red')
        self.assertTrue('red' in self.my_dojo.all_rooms['office'].keys())

    def test_add_person_successfully(self):
        initial_fellow_count = len(self.my_dojo.all_persons['fellow'])
        self.my_dojo.add_person('Mike', 'fellow')
        new_fellow_count = len(self.my_dojo.all_persons['fellow'])
        self.assertEqual(new_fellow_count - initial_fellow_count, 1)

    def test_person_added(self):
        self.assertFalse('mike' in self.my_dojo.all_persons['fellow'])
        self.my_dojo.add_person('Mike', 'Fellow')
        self.assertTrue('mike' in self.my_dojo.all_persons['fellow'].keys())

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
            self.assertIn('mike', self.my_dojo.all_rooms['office']['mango'].members)

    def test_unallocated(self):
        self.my_dojo.add_person('Mike', 'staff')
        self.assertFalse(self.my_dojo.all_persons['staff']['mike'].accommodation)

    def test_list_rooms(self):
        self.assertEqual(len(self.my_dojo.all_rooms['office']), 0)
        self.assertEqual(len(self.my_dojo.all_rooms['living_space']), 0)
        self.my_dojo.create_room('office', 'Mango')
        self.my_dojo.create_room('living', 'Banana')
        self.assertIn('mango', self.my_dojo.list_rooms('office'))
        self.assertIn('banana', self.my_dojo.list_rooms('living'))

    def test_rand_office_gen(self):
        pass

    def test_reallocate_person(self):
        self.my_dojo.create_room('office', 'mango')
        self.my_dojo.create_room('living', 'pine')
        self.my_dojo.add_person('john doe', 'staff', 'y')
        self.my_dojo.add_person('pete bet', 'fellow', 'y')
        self.assertIn('john doe', self.my_dojo.all_rooms['office']['mango'].members)
        self.assertIn('pete bet', self.my_dojo.all_rooms['living_space']['pine'].members)
        self.my_dojo.create_room('office', 'banana')
        self.my_dojo.create_room('living', 'apple')
        self.my_dojo.reallocate_person('john doe', 'banana')
        self.my_dojo.reallocate_person('pete bet', 'apple')
        self.assertIn('john doe', self.my_dojo.all_rooms['office']['banana'].members)
        self.assertIn('pete bet', self.my_dojo.all_rooms['living_space']['apple'].members)

    def test_load_people(self):
        print_file = 'OLUWAFEMI SULE FELLOW Y \nDOMINIC WALTERS STAFF '
        f = open('test.txt', 'w')
        f.write(print_file)
        f.close()
        self.my_dojo.load_people('test.txt')
        print(self.my_dojo.all_persons['fellow'].keys())
        self.assertIn('OLUWAFEMI SULE'.lower(), self.my_dojo.all_persons['fellow'].keys())
        self.assertIn('DOMINIC WALTERS'.lower(), self.my_dojo.all_persons['staff'].keys())

    def test_check_space_in_room(self):
        self.my_dojo.create_room('office', 'mango')
        self.my_dojo.add_person('mercy', 'staff')
        self.my_dojo.add_person('tom', 'staff')
        self.my_dojo.add_person('mary', 'staff')
        self.my_dojo.add_person('john', 'staff')
        self.my_dojo.add_person('jane', 'staff')
        self.my_dojo.add_person('tim', 'staff')
        self.assertFalse(self.my_dojo.check_space_in_room('mango', 'office'))
