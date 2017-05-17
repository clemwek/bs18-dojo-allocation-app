#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file serve as a starting point for a Python console script.
"""
from allo.room.room import Room, Office, LivingSpace
from allo.person.person import Person, Fellow, Staff


class Dojo(object):
    """
    Class Dojo the main entry point to a110-cli
    """
    def __init__(self):
        self.all_persons = {}
        self.all_fellows = []
        self.all_staff = []
        self.all_rooms = {}
        self.all_offices = []
        self.all_living_space = []
        self.room_allocation = {
            "office": {},
            "living_space": {}
        }

    def create_room(self, room_type, room_name):
        try:
            room_type = room_type.lower()
            room_name = room_name.lower()
            if room_name in self.all_rooms.keys():
                return "Sorry, {} room name has been taken.".format(room_name)
            if room_type == 'office':
                new_office = Office(room_name)
                self.all_rooms[room_name] = new_office
                self.room_allocation['office'][room_name] = []
                return "{} - office added successfully".format(room_name)
            elif room_type == 'living':
                new_living = LivingSpace(room_name)
                self.all_rooms[room_name] = new_living
                self.room_allocation['living_space'][room_name] = []
                return "{} - living space added successfully".format(room_name)
            else:
                return "A room can only be office or living space"
        except ValueError as e:
            return "The value passed is not a string"

    def add_person(self, person_name, person_kind, accomodation='N'):
        try:
            person_name = person_name.lower()
            person_kind = person_kind.lower()
            accomodation = accomodation.lower()
            if person_name in self.all_persons.keys():
                return "Sorry, {} person name has been added.".format(person_name)
            if person_kind == 'fellow':
                new_fellow = Fellow(person_name)
                print(new_fellow)
                self.all_persons[person_name] = new_fellow
                # allocate a room randomly
                return "{} - fellow added successfully".format(person_name)
            elif person_kind == 'staff':
                new_staff = Staff(person_name)
                self.all_persons[person_name] = new_staff
                # Allowcate some ramdom room
                return "{} - staff space added successfully".format(person_name)
            else:
                return "A room can only be office or living space"
        except ValueError as e:
            return "The value passed is not a string"


if __name__ == "__main__":
    dojo = Dojo()
    print(dojo.all_persons)
    dojo.add_person("Mike", "fellow")
    print(dojo.all_persons['mike'].person_name)
