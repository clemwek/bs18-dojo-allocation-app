#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Room(object):
    def __init__(self, room_name, room_type, capacity=0):
        self.capacity = capacity
        self.room_name = room_name
        self.room_type = room_type
        self.occupants = []
        self.members = []


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type='office', capacity=6)
        self.room_name = room_name


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type='office', capacity=4)
        self.room_name = room_name
