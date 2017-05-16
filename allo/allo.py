#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
from allo.room import room


class Dojo(object):
    """
    Class Dojo the main entry point to a110-cli
    """
    def __init__(self):
        self.all_persons = []
        self.all_fellows = []
        self.all_staff = []
        self.all_rooms = []
        self.all_offices = []
        self.all_living_space = []
        self.room_allocation = {
            "office": {},
            "living_space": {}
        }

    def create_room(self, room_type, room_name):
        room_type = room_type.lower()
        room_name = room_name.lower()
        if room_name in self.all_rooms:
            return "Sorry, {} room name has been taken.".format(room_name)
        if room_type == 'office':
            new_office = room.Office()
            self.all_rooms.append(new_office[0])
            self.room_allocation['office'][room_name] = []
            return "{} - office added successfully".format(room_name)
        elif room_type == 'living':
            self.all_rooms.append(room_name)
            self.room_allocation['living_space'][room_name] = []
            return "{} - living space added successfully".format(room_name)
        else:
            return "A room can only be office or living space"

