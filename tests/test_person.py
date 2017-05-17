import unittest
from allo.person.person import Person, Fellow, Staff


class TestPerson(unittest.TestCase):
    def test_can_be_created(self):
        new_fellow = Fellow('Mike')
        new_staff = Staff('jane')
        self.assertIsInstance(new_fellow, Fellow)
        self.assertIsInstance(new_staff, Staff)
