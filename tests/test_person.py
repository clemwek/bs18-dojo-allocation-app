import unittest
from allo.person import person


class TestPerson(unittest.TestCase):
    def test_can_be_created(self):
        new_person = person.Person()
        self.assertIsInstance(new_person, person.Person)


class TestFellow(unittest.TestCase):
    pass


class TestOffice(unittest.TestCase):
    pass
