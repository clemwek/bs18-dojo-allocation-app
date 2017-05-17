#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, person_name, person_kind, accomodation='N'):
        self.person_name = person_name
        self.person_kind = person_kind
        self.accormodation = accomodation


class Fellow(Person):
    def __init__(self, person_name):
        super(Fellow, self).__init__(person_name, person_kind="fellow")
        self.person_name = person_name


class Staff(Person):
    def __init__(self, person_name):
        super(Staff, self).__init__(person_name, person_kind="staff")
        self.person_name = person_name
