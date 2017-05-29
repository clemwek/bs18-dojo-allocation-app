class Person(object):
    def __init__(self, person_name, person_kind, accommodation=False, office=False):
        self.person_name = person_name
        self.person_kind = person_kind
        self.accommodation = accommodation
        self.office = office


class Fellow(Person):
    def __init__(self, person_name):
        super(Fellow, self).__init__(person_name, person_kind="fellow")


class Staff(Person):
    def __init__(self, person_name):
        super(Staff, self).__init__(person_name, person_kind="staff")
