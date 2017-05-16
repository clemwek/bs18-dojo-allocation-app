#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Room(object):
    def __init__(self, capacity=0):
        self.capacity = capacity


class Office(Room):
    def __init__(self):
        super(Office, self).__init__(capacity=6)

    def create_office(self, office_name, room_type):
        office_name = office_name.lower()
        room_type = room_type.lower()
        return [office_name, room_type, self.capacity]


class LivingSpace(Room):
    def __init__(self):
        super().__init__(capacity=4)

    def create_living_space(self, office_name, room_type):
        return [office_name, room_type, self.capacity]
